from django.urls import path
from . import views

urlpatterns = [
    path('stafflogin', views.stafflogin, name="stafflogin"),
    path('checkStaff', views.checkStaff, name="checkStaff"),
    path('bikeoperations', views.add_bike, name='bikeoperations'),
    path('upload', views.upload, name='upload'),
]
