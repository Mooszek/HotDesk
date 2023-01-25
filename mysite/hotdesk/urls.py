from django.urls import path
from .views import (
    TodaysReservationListView,
    ReservationListView,
    ReservationHistoryListView, 
    ReservationDetailView, 
    ReservationDeleteView,
    # ReservationCreateView, 
    # ReservationUpdateView, 
)
from . import views

urlpatterns = [
    path('', TodaysReservationListView.as_view(), name='hotdesk-homepage'),
    path('reservations/', ReservationListView.as_view(), name='hotdesk-reservations'),
    path('reservations_history/', ReservationHistoryListView.as_view(), name='hotdesk-reservations-history'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='hotdesk-reservation'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='hotdesk-reservation-delete'),
    path('reservation_new/', views.reservation_function, name='hotdesk-reservations-new'),
    # path('reservations/new/', ReservationCreateView.as_view(), name='hotdesk-new-reservation'),
    # path('reservations/<int:pk>/update/', ReservationUpdateView.as_view(), name='hotdesk-reservation-update'),
]