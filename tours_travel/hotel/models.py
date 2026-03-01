from django.db import models
from core.models import Address

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    # Multiple addresses via core.Address.hotel

    def __str__(self):
        return self.name
