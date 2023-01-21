from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='hotdesk-index'),
    path('reservation/new/', views.new_reservation, name='hotdesk-new-reservation'),
    path('reservations/', views.reservations, name='hotdesk-reservations'),
    path('reservation/<int:reservation_id>/', views.reservation, name='hotdesk-reservation'),
    path('about/', views.about, name='hotdesk-about'),
]