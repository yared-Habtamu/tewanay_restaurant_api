from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Hotel Manager'),
        ('CUSTOMER', 'Customer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CUSTOMER')
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username
