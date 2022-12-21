from django.shortcuts import render
from django.http import HttpResponse
from hotdesk.models import Reservation

# Create your views here.

def index(request):
    return HttpResponse("This will be hotdesking app")

def reservation(request, reservation_id):
    reservation_object = Reservation.objects.get(pk=reservation_id)
    start_date = reservation_object.start_date
    end_date = reservation_object.end_date
    response = f"Reservation ID: {reservation_id} Start Date: {start_date} End Date: {end_date}"
    return HttpResponse(response)

