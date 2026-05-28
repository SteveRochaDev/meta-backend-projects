from django.db import models
from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.booking_date.date()}"