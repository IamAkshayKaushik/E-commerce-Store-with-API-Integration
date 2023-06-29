from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
