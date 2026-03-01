from django.db import models
from core.models import Package  # or update import if in another app

class GalleryImage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.package.name}"
