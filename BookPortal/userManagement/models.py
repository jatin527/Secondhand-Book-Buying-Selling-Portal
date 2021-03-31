from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date

# Create your models here.


class customerUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    name = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)
    city = models.CharField(max_length=15)
    username = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['city', 'name', 'contact_no']

    def __str__(self):
        return "{}".format(self.email)
