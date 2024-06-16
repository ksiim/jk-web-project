import os
from django.contrib.auth.models import AbstractUser
from django.db import models

PROGRAMMING_LANGUAGES = [
    ("python", "Python"),
    ("java", "Java"),
    ("cpp", "C++"),
    ("csharp", "C#")
]

def get_background_image_choices():
    bg_dir = os.path.join('static', 'img', 'backgrounds')
    backgrounds = [(f, f) for f in os.listdir(bg_dir) if os.path.isfile(os.path.join(bg_dir, f))]
    return backgrounds

class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    
    def __str__(self):
        return self.name

class Person(AbstractUser):
    password = models.CharField(max_length=255, verbose_name='Пароль')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    year = models.IntegerField(null=True, blank=True, verbose_name='Год обучения')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Аватар')
    profile_background = models.CharField(max_length=255, choices=get_background_image_choices(), null=True, blank=True, verbose_name='Фон профиля', default='profile_background.jpg')
    programming_language = models.TextField(choices=PROGRAMMING_LANGUAGES, null=True, blank=True, verbose_name='Язык программирования')
    tg_url = models.CharField(max_length=50, null=True, blank=True, verbose_name='Telegram')
    discord_url = models.CharField(max_length=50, null=True, blank=True, verbose_name='Discord')
    github_url = models.CharField(max_length=50, null=True, blank=True, verbose_name='Github')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, verbose_name='Группa', null=True)
    
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

    class Meta:
        ordering = ['-date_joined']
