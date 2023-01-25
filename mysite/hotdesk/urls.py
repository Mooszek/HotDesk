from django.urls import path
from .views import (
    TodaysReservationListView,
    ReservationListView, 
    ReservationDetailView, 
    # ReservationCreateView, 
    # ReservationUpdateView, 
    ReservationDeleteView,
)
from . import views

urlpatterns = [
    path('', TodaysReservationListView.as_view(), name='hotdesk-index'),
    # path('reservations/new/', ReservationCreateView.as_view(), name='hotdesk-new-reservation'),
    path('reservations/', ReservationListView.as_view(), name='hotdesk-reservations'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='hotdesk-reservation'),
    # path('reservations/<int:pk>/update/', ReservationUpdateView.as_view(), name='hotdesk-reservation-update'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='hotdesk-reservation-delete'),
    path('reservation_new/', views.reservation_function, name='hotdesk-reservations-new'),
]