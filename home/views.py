from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Parking
from django.contrib import messages

# Create your views here.


def index(request):
    # return HttpResponse('this is home page')
    if (request.method == "POST"):
        state = request.POST.get('state')
        vehicle_no = request.POST.get('vehicle_no')
        vehicle_type = request.POST.get('vehicle_type')

        parking = Parking(state=state, vehicle_no=vehicle_no,
                          vehicle_type=vehicle_type, park_date=datetime.now())

        try:
            parking.save()
            messages.success(request, 'Your slot has been booked...')
        except IntegrityError as e:
            messages.error(request, ' Invalid Entry...')

    # all_vehicle = Parking.objects.all().count()
    two_wheel = Parking.objects.filter(vehicle_type="2 Wheeler").count()
    four_wheel = Parking.objects.filter(vehicle_type="4 Wheeler").count()

    context = {'total': (two_wheel+four_wheel),
               'two_wheel': 50-two_wheel, 'four_wheel': 50-four_wheel, 'booked_two': two_wheel, 'booked_four': four_wheel}
    return render(request, 'index.html', context)


def parking(request):
    all_vehicle = Parking.objects.all()
    context = {'vehicles': all_vehicle}
    return render(request, 'parking.html', context)


def reciept(request, id):
    data = Parking.objects.get(pk=id)
    context = {'vehicle': data}
    return render(request, 'reciept.html', context)


def delete_data(request, id):
    dele = Parking.objects.get(pk=id)
    dele.delete()
    messages.error(request, ' Slot has been removed...')
    return redirect('/parking')