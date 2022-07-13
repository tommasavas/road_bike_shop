from django.http import Http404
from django.shortcuts import get_list_or_404, redirect, render
from .models import *
from django.contrib.auth.models import User, auth
from datetime import datetime

# Create your views here.

def index(request, *args, ** kwargs):
    bikes = Bike.objects.all()
    tags = Tag.objects.values('tag').distinct()
    context = {
        'bikes': bikes,
        'tags': tags
    }
    return render(request, "index.html", context)

def cat(request, id, *args, **kwargs):
    bikes=Tag.objects.filter(tag=id)
    return render(request, 'category.html', {'bikes': bikes})
    
def description_view(request, id, *args, **kwargs):
    bike = Bike.objects.get(id=id)
    context = {
        'bike': bike,
    }
    return render(request, 'description.html', context)

def add(request, id, *args, **kwargs):
    # print(request.path())
    if (not request.user.is_authenticated):
        return redirect('../../../login/login')
    user_obj = User.objects.filter(username=request.user)
    bike_obj = Bike.objects.filter(id=id)
    check = MyCart.objects.filter(user=request.user,bike_id=id)
    if len(check) != 0:
        print("Bike Exits!!")
    else:
        obj = MyCart.objects.create(
            user=user_obj[0], bike=bike_obj[0], added_date=datetime.now())
        obj.save()
    return redirect('../../../')

def remove(request, id,*args, **kwargs):
    cart_obj = MyCart.objects.get(bike=id)
    cart_obj.delete()
    
    return redirect('cart')

def about_us_view(request, *args, **kwargs):
    # about us
    return render(request, "aboutus.html", {})

def cart_view(request, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    cart_obj = MyCart.objects.filter(user=user_obj)
    img = list()
    for item in cart_obj:
        bikeObj = Bike.objects.get(id=item.bike.id)
        img.append(bikeObj)

    con = zip(cart_obj, img)
    context = {
        'con': con
    }

    return render(request, "cart.html", context)

def order(request,id, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    print(id)
    bike_obj = Bike.objects.get(id = id)
    obj = MyOrder.objects.create(user = user_obj, bike = bike_obj)
    obj.save()
    cart_obj = MyCart.objects.filter(bike = bike_obj)
    cart_obj.delete()
    bike_obj.instock = False
    bike_obj.save()
    return redirect('cart')

def order_view(request, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    order_obj = MyOrder.objects.filter(user=user_obj)
    img = list()
    for item in order_obj:
        bikeObj = Bike.objects.get(id=item.bike.id)
        img.append(bikeObj)

    con = zip(order_obj, img)
    context = {
        'con': con
    }
    return render(request,"order.html",context)