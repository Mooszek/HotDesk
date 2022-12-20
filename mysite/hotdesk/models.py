from django.db import models

# Create your models here.
class Room(models.Model):
    room_id = models.IntegerField(unique=True)
    room_name = models.CharField(unique=True, max_length=20)
    desk_capacity = models.IntegerField()

class Desk(models.Model):
    desk_id = models.IntegerField(unique=True)
    desk_label = models.CharField(unique=True, max_length=20)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL)
    monitors_count = models.IntegerField(default=0)
    reservation_flag = models.BooleanField(default=False)

class Reservation(models.Model):
    reservation_id = models.IntegerField(unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()