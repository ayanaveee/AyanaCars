# Generated by Django 5.2.4 on 2025-07-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_car_color_car_engine_volume_car_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
