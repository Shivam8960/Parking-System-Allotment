# Generated by Django 4.1.2 on 2022-11-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_remove_parking_id_parking_vehicle_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="parking",
            name="park_time",
        ),
        migrations.AlterField(
            model_name="parking",
            name="park_date",
            field=models.DateTimeField(),
        ),
    ]
