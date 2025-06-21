from django.db import models
from django.utils import timezone

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Booking_table(models.Model):
    name = models.CharField(max_length=100)
    num_of_guests = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
