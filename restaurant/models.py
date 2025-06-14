from django.db import models
import datetime
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    guestes_num = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateField(default=datetime.date.today())  

    def __str__(self):
        return self.name


class Booking(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name