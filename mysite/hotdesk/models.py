from django.db import models

# Create your models here.
class Room(models.Model):
    #room_id = models.IntegerField(unique=True)
    room_name = models.CharField(unique=True, max_length=20)
    desk_capacity = models.IntegerField()

    def __str__(self) -> str:
        return self.room_name

class Desk(models.Model):
    desk_label = models.CharField(unique=True, max_length=20)
    room = models.ForeignKey(Room, default=None, blank= True, null=True, on_delete=models.SET_NULL)
    monitors_count = models.IntegerField(default=0)
    reservation_flag = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.desk_label

class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"Reservation ID: {self.id}"