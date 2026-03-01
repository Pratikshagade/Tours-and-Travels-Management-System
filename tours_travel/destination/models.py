from django.db import models
from core.models import Address

class Destination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name='destination',
    )

    def __str__(self):
        return self.name
