from django.contrib import admin
from .models import *

# Register your models here.


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('producer', 'speciality',)


class BikeAdmin(admin.ModelAdmin):
    list_display = ('bike_name', 'bike_producer',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)


class MyCartAdmin(admin.ModelAdmin):
    list_display = ('bike', 'user')


class MyOrderAdmin(admin.ModelAdmin):
    list_display = ('bike', 'user', 'date')


admin.site.register(Producer, ProducerAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(MyCart, MyCartAdmin)
admin.site.register(MyOrder, MyOrderAdmin)
