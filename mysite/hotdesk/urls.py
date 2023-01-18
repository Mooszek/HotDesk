from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='hotdesk-index'),
    path('about/', views.about, name='hotdesk-about'),
    path('<int:reservation_id>/', views.reservation, name='hotdesk-reservation'),
]