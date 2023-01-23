from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from hotdesk.models import Reservation

# Create your views here.

def index(request):
    context = {'page_text':"Main page",}
    return render( request, 'hotdesk/index.html', context)

def new_reservation(request):
    context = {'page_text':"Make new reservation",}
    return render( request, 'hotdesk/new_reservation.html', context)

def reservations(request):
    context = {'page_text':"Previous reservations",}
    return render( request, 'hotdesk/reservations.html', context)

def about(request):
    context = {'page_text':"About Page",}
    return render( request, 'hotdesk/about.html', context)

def reservation(request, reservation_id):
    try:
        reservation_object = Reservation.objects.get(pk=reservation_id)
        start_date = reservation_object.start_date
        end_date = reservation_object.end_date
        response = f"Reservation ID: {reservation_id} Start Date: {start_date} End Date: {end_date}"
    except Reservation.DoesNotExist:
        raise Http404("Reservation does not exist")
    return render(request, 'hotdesk/reservation.html', {'reservation': response,})

