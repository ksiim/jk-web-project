from django.contrib.auth.models import AbstractUser
from django.db import models

PROGRAMMING_LANGUAGES = [
    ("python", "Python"),
    ("java", "Java"),
    ("cpp", "C++"),
    ("csharp", "C#")
]

class Person(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    specialization = models.TextField(null=True, blank=True)
    programming_language = models.TextField(choices=PROGRAMMING_LANGUAGES, null=True, blank=True)
    
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
