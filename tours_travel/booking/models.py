from django.db import models
from django.conf import settings
from core.models import Address
from hotel.models import Hotel
from destination.models import Destination
from food.models import Food
from core.models import Package  # If you want to link to the main package model


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Main package and related info
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='booking_packages')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='booking_packages')
    foods = models.ManyToManyField(Food, related_name='booking_packages', blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='booking_package',null=True)

    # Booking meta info
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    # Razorpay fields (optional now, needed later for confirmation)
    razorpay_order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    razorpay_signature = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
