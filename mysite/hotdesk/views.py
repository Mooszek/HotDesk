
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from hotdesk.models import Reservation, Room, Desk
from datetime import date

from .forms import SearchRoomForm

# Create your views here.
@login_required
def index(request):
    context = {'page_text':"Main page",}
    return render( request, 'hotdesk/index.html', context)


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

# # not used
# class ReservationCreateView(LoginRequiredMixin, CreateView):
#     model = Reservation
#     fields = [ 'desk', 'start_date', 'end_date']
#     template_name = 'hotdesk/new_reservation.html'
#     success_url = reverse_lazy('hotdesk-reservations')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# #not used
# class ReservationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Reservation
#     fields = [ 'desk', 'start_date', 'end_date']
#     template_name = 'hotdesk/new_reservation.html'
#     success_url = reverse_lazy('hotdesk-reservations')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         reservation = self.get_object()
#         if self.request.user == reservation.user:
#             return True
#         return False


class ReservationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reservation
    template_name = 'hotdesk/reservation_delete.html'
    success_url = '/hotdesk/reservations'

    def test_func(self):
        reservation = self.get_object()
        if self.request.user == reservation.user:
            return True
        return False

@login_required
def reservation_function(request):

    #submit data preserved from previous request  on form
    submit_data = request.POST.get('room')
    room_data = SearchRoomForm(request.POST or None)

    if request.POST.get('room'):
        selected_room= request.POST.get('room')
        selected_start_date = request.POST.get('start_date')
        selected_end_date = request.POST.get('end_date')

    if 'search_room' in request.POST:

        if selected_end_date < selected_start_date:
            messages.warning(request, f"End date can't be earlier than start date!")
            context = {
                'room_data' : room_data,
            }
            return render(request, 'hotdesk/reservation_new.html', context) 

        available_desks = Desk.objects.filter(room__id = selected_room).exclude(
            reservation__start_date__lte=selected_end_date,
            reservation__end_date__gte = selected_start_date)        

    elif 'reserve_desk_number' in request.POST:
        desk_id = request.POST.get('reserve_desk_number')

        Reservation.objects.create(user=request.user, start_date= selected_start_date, end_date=selected_end_date, desk_id = desk_id)

        context = {
            'user' : request.user,
            'selected_room' : selected_room,
            'selected_start_date' : selected_start_date,
            'selected_end_date' : selected_end_date,
            'submit_data' : submit_data
        }
        return render(request, 'hotdesk/reservations.html', context) 
    
    else:
        available_desks = ''
        selected_room = ''
        selected_start_date = ''
        selected_end_date = ''

    context = {
        'available_desks' : available_desks,
        'room_data' : room_data,
        'selected_room' : selected_room,
        'selected_start_date' : selected_start_date,
        'selected_end_date' : selected_end_date,
        'submit_data' : submit_data
    }

    return render(request, 'hotdesk/reservation_new.html', context)