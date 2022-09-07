from django.contrib.auth.models import AbstractUser
from django.db import models


from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False, max_length=256)
    phone = models.CharField(max_length=25, blank=True)
    portfolio_email = models.EmailField(blank=True, max_length=256)
    about = models.TextField(blank=True)
    image = models.CharField(max_length=1000, blank=True)
    theme = models.CharField(max_length=256, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email