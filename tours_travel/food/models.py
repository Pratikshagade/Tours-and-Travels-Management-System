from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # ✅ Must be here
    price = models.DecimalField(max_digits=8, decimal_places=2)  # ✅ Must be here
    image = models.ImageField(upload_to='food/', null=True, blank=True)

    def __str__(self):
        return self.name
