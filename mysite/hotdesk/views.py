#from django.http import HttpResponse, Http404
#from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hotdesk.models import Reservation
from datetime import date

# Create your views here.
@login_required
def index(request):
    context = {'page_text':"Main page",}
    return render( request, 'hotdesk/index.html', context)

#class based view for homepage


# @login_required
# def new_reservation(request):
#     context = {'page_text':"Make new reservation",}
#     return render( request, 'hotdesk/new_reservation.html', context)

# @login_required
# def reservations(request):
#     context = {'page_text':"Previous reservations",}
#     return render( request, 'hotdesk/reservations.html', context)

#class based view for previous reservations
class TodaysReservationListView(ListView):
    model = Reservation
    template_name = 'hotdesk/index.html'
    context_object_name = 'reservations'
    ordering = ['start_date']

    def get_queryset(self):
        return Reservation.objects.filter(start_date__lte = date.today(), end_date__gte = date.today())

class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'hotdesk/reservations.html'
    context_object_name = 'reservations'
    ordering = ['start_date']

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

#class to see single reservation
class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'hotdesk/reservation.html'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

#class to create single reservation
class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    fields = [ 'desk', 'start_date', 'end_date']
    template_name = 'hotdesk/new_reservation.html'
    success_url = reverse_lazy('hotdesk-reservations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#class to update single reservation
class ReservationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reservation
    fields = [ 'desk', 'start_date', 'end_date']
    template_name = 'hotdesk/new_reservation.html'
    success_url = reverse_lazy('hotdesk-reservations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        reservation = self.get_object()
        if self.request.user == reservation.user:
            return True
        return False


class ReservationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reservation
    template_name = 'hotdesk/reservation_delete.html'
    success_url = '/hotdesk/reservations'

    def test_func(self):
        reservation = self.get_object()
        if self.request.user == reservation.user:
            return True
        return False

# pick room
# class ReservationCreateView(CreateView):
#     model = Room
#     fields = [ 'room', 'start_date', 'end_date']
#     template_name = 'hotdesk/new_reservation.html'


def about(request):
    context = {'page_text':"About Page",}
    return render( request, 'hotdesk/about.html', context)

# @login_required
# def reservation(request, reservation_id):
#     try:
#         reservation_object = Reservation.objects.get(pk=reservation_id)
#         start_date = reservation_object.start_date
#         end_date = reservation_object.end_date
#         response = f"Reservation ID: {reservation_id} Start Date: {start_date} End Date: {end_date}"
#     except Reservation.DoesNotExist:
#         raise Http404("Reservation does not exist")
#     return render(request, 'hotdesk/reservation.html', {'reservation': response,})

