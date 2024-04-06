from django.contrib.auth.models import AbstractUser
from django.db import models

class Person(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='persons',
        blank=True,
        help_text='The groups this person belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='persons',
        blank=True,
        help_text='Specific permissions for this person.',
        verbose_name='user permissions',
    )