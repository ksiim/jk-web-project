from django.contrib.auth.models import AbstractUser
from django.db import models

PROGRAMMING_LANGUAGES = [
    ("python", "Python"),
    ("java", "Java"),
    ("cpp", "C++"),
    ("csharp", "C#")
]

SPEcialization = [
    ("backend", "Backend"),
    ("frontend", "Frontend"),
    ("fullstack", "Fullstack"),
    ("mobile", "Mobile")
]

class Person(AbstractUser):
    password = models.CharField(max_length=255, verbose_name='Пароль')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    experience = models.IntegerField(null=True, blank=True, verbose_name='Опыт работы')
    specialization = models.TextField(max_length=255, null=True, blank=True, verbose_name='Специализация')
    programming_language = models.TextField(choices=PROGRAMMING_LANGUAGES, null=True, blank=True, verbose_name='Язык программирования')
    
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
