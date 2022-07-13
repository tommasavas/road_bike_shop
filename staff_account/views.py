from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import request
from bike_store_app.models import *

# Create your views here.

def stafflogin(request, *args, ** kwargs):

    return render(request, 'stafflogin.html', {})

def checkStaff(request, *args, **kwargs):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', False)
        password = request.POST['password']
        user = auth.authenticate(
            username=user_name, password=password, staff=True)
        if user is not None:
            print(request.user)
            auth.login(request, user)
            return render(request, 'bikeoperations.html', {})
    return redirect('stafflogin')

def add_bike(request, *args, **kwargs):
    bike = Bike.objects.all()
    producer = Producer.objects.all()
    print("\n bike \n")
    context = {
        'bike': bike,
        'producer': producer,
    }
    return render(request, "bikeoperations.html", context)

def upload(request, *args, **kwargs):
    if request.method == 'POST':
        bike_name = request.POST['bike_name']
        bike_producer = request.POST['bike_producer']
        producer = Producer.objects.get(id = bike_producer.split()[0])
        description = request.POST['description']
        price = request.POST['price']
        image = request.POST['image']
        newbike = Bike.objects.create(bike_name=bike_name,
                                    price=price,
                                    bike_producer=producer,
                                    image=image,
                                    description = description
                                    )
        print(bike_name, bike_producer, description, price)
        newbike.save()
        bike = Bike.objects.all()
    else:
        return redirect('home')

    context = {
        'bike': bike,
    }
    return render(request, "bikeoperations.html", context)
