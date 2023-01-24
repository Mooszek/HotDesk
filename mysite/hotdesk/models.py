from django.db import models
from users.models import User

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(unique=True, max_length=20)
    room_layout = models.ImageField(default=None, blank=True, upload_to='room_layout')
    is_active = models.BooleanField(default=1)

    def __str__(self) -> str:
        return self.room_name

class Desk(models.Model):
    desk_label = models.CharField(unique=True, max_length=20)
    room = models.ForeignKey(Room, default=None, blank= True, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=1)
    is_deleted = models.BooleanField(default=0)

    def __str__(self) -> str:
        return self.desk_label

class Reservation(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    desk = models.ForeignKey(Desk, default = None, blank = True, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default="Active")
    is_deleted = models.BooleanField(default=0)

    def __str__(self) -> str:
        return f"Reservation ID: {self.id}"