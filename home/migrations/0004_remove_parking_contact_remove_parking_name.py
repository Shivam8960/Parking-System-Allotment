# Generated by Django 4.1.2 on 2022-11-17 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_parking_park_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="parking",
            name="contact",
        ),
        migrations.RemoveField(
            model_name="parking",
            name="name",
        ),
    ]