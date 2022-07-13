# Generated by Django 4.0.6 on 2022-07-13 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_store_app', '0007_alter_bike_image_alter_mycart_added_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 13, 15, 47, 14, 304245)),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 13, 15, 47, 14, 305295)),
        ),
    ]