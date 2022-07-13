from django.db import models
from django.db import models
import os
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

User = get_user_model()


# Artist
class Producer(models.Model):

    producer = models.CharField(max_length=300 , null = False, blank = False)
    speciality = models.CharField(max_length=300,null = False, blank = False)

    def __str__(self):
        return self.producer

# Art
class Bike(models.Model):
    bike_name = models.CharField(max_length=50, null=False, blank=False)
    bike_producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=os.path.join("media/"))
    price = models.FloatField(null=False, blank=False)
    instock = models.BooleanField(null = False,blank=False, default=True)
    description = models.TextField(null=False, blank=False)


# TAGs
class Tag(models.Model):
    tag = models.CharField(max_length=300, null=False)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)


# Cart Table
class MyCart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=datetime.now())


# Order Table
class MyOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())