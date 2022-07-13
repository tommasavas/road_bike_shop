from django.contrib import admin
from .models import *
# Register your models here.


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('producer', 'speciality',)


class BikeAdmin(admin.ModelAdmin):
    list_display = ('bike_name', 'bike_producer',)


admin.site.register(Producer, ProducerAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Tag)
admin.site.register(MyCart)
admin.site.register(MyOrder)
