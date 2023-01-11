from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=10, default='WOMEN', choices=(('WOMEN', 'WOMEN'), ('MEN', 'MEN')))
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, null=True)  # number validasiyasi etmek
    address = models.CharField(max_length=225, null=True)
    country = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(default=True, null=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    additional = models.TextField(null=True)
    last_login_time = models.DateTimeField(default=datetime.now)

    class Meta:
        indexes = [
            models.Index(fields=['first_name'])
        ]

