from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model extending AbstractUser.
    """
    phone = models.CharField(max_length=20, blank=True, null=True)
    # add additional fields here

    def __str__(self):
        return self.username
