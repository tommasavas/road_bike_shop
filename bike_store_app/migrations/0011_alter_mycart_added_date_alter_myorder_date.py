# Generated by Django 4.0.6 on 2022-07-13 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_store_app', '0010_remove_tag_bike_alter_mycart_added_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 14, 0, 3, 52, 949000)),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 14, 0, 3, 52, 949000)),
        ),
    ]
