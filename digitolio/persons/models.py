from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Person(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)