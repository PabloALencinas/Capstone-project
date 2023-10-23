from django.db import models
from django.utils import timezone

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    booking_date = models.DateField(default=timezone.now)
        
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self):
        return f'{self.name}: {self.booking_date}'


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f'{self.title}: ${self.price:.2f}'