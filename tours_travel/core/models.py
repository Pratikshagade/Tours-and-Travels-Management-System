from django.db import models
from django.conf import settings

class Address(models.Model):
    """
    Generic address, linked to User or Hotel.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='addresses',
        null=True,
        blank=True,
    )
    hotel = models.ForeignKey(
        'hotel.Hotel',
        on_delete=models.CASCADE,
        related_name='addresses',
        null=True,
        blank=True,
    )
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='packages/', null=True, blank=True)

    destination = models.ForeignKey(
        'destination.Destination',
        on_delete=models.CASCADE,
        related_name='packages'
    )

    # ✅ Many-to-many relationships for services
    hotels = models.ManyToManyField('hotel.Hotel', blank=True, related_name='packages')
    foods = models.ManyToManyField('food.Food', blank=True, related_name='packages')
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
