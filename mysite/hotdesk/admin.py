from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Desk, Room, Reservation

admin.site.register(Desk)
admin.site.register(Room)
admin.site.register(Reservation)

# Register your models here.
