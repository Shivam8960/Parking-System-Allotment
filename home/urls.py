from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("parking/", views.parking, name='home'),
    path("delete/<int:id>", views.delete_data, name='deleteData'),
    path("<int:id>/", views.reciept, name='downloadReciept')
]