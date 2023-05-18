from django.contrib import admin
from home.models import Parking
# Register your models here.
admin.site.register(Parking)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'state', 'vehicle_no', 'vehicle_type', 'park_time', 'park_date', 'park_price')
