from django.urls import path
from .views import (
    TodaysReservationListView,
    ReservationListView, 
    ReservationDetailView, 
    ReservationCreateView, 
    ReservationUpdateView, 
    ReservationDeleteView
)
from . import views

urlpatterns = [
    #path('', views.index, name='hotdesk-index'),
    path('', TodaysReservationListView.as_view(), name='hotdesk-index'),
    #path('reservation/new/', views.new_reservation, name='hotdesk-new-reservation'),
    path('reservations/new/', ReservationCreateView.as_view(), name='hotdesk-new-reservation'),
    #path('reservations/', views.reservations, name='hotdesk-reservations'),
    path('reservations/', ReservationListView.as_view(), name='hotdesk-reservations'),
    #path('reservation/<int:reservation_id>/', views.reservation, name='hotdesk-reservation'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='hotdesk-reservation'),
    path('reservations/<int:pk>/update/', ReservationUpdateView.as_view(), name='hotdesk-reservation-update'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='hotdesk-reservation-delete'),
    path('about/', views.about, name='hotdesk-about'),
]