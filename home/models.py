from django.db import models
from datetime import datetime, time

# Create your models here.


class Parking(models.Model):

    vehicle_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=4)
    vehicle_no = models.CharField(max_length=6, unique=True)
    vehicle_type = models.CharField(max_length=5)
    park_date = models.DateTimeField()
    park_price = models.IntegerField(default=20)

    def __str__(self):
        return self.vehicle_no.upper()

    @property
    def date_till(self):
        today = datetime.now()
        return today

    @property
    def bills(self):
        today = datetime.now().hour
        park_day = (self.park_price+20) if (today-self.park_date.hour) >= 2 else self.park_price
        # day = today-self.park_date.hour
        return park_day
