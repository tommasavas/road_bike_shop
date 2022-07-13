from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',index , name = 'index'),
    path('aboutus/', about_us_view, name = 'about'),
    path('cart/', cart_view, name = 'cart'),
    path('order/', order_view, name = 'order'),
    path('login/',include('login.urls')),
    path('description/<int:id>/', description_view, name = 'description'),
    path('description/<int:id>/add', add, name = 'add'),
    path('cart/order/<int:id>', order, name = 'order'),
    path('cart/remove/<int:id>', remove, name = 'remove'),
    path('staffaccount/',include('staff_account.urls')),    
    path('cat/<str:id>', cat, name = 'cat'),
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)