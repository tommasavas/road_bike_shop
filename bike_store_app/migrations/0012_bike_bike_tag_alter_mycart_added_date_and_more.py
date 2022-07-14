# Generated by Django 4.0.6 on 2022-07-13 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_store_app', '0011_alter_mycart_added_date_alter_myorder_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='bike_tag',
            field=models.ManyToManyField(help_text='Išrinkite žanrą(us) šiai knygai', to='bike_store_app.tag'),
        ),
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 14, 0, 14, 20, 892990)),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 14, 0, 14, 20, 892990)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(help_text='Įveskite knygos žanrą (pvz. detektyvas)', max_length=200, verbose_name='Pavadinimas'),
        ),
    ]
