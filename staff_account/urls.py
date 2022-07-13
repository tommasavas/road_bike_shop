from django.urls import path
from . import views

urlpatterns = [
    path('',views.stafflogin, name="stafflogin"),
    path('checkStaff/',views.checkStaff, name="checkStaff"),
    path('artoperations', views.add_bike, name = 'bikeoperations'),
    path('upload',views.upload,name='upload'),
]