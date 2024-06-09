from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

PROGRAMMING_LANGUAGES = [
    ("python", "Python"),
    ("java", "Java"),
    ("cpp", "C++"),
    ("csharp", "C#")
]

CATEGORY = [
    ('web', 'Web'),
    ('mobile', 'Mobile'),
    ('desktop', 'Desktop'),
    ('game', 'Game'),
    ('ml', 'Machine Learning'),
    ('ds', 'Data Science'),
    ('cv', 'Computer Vision')]

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', verbose_name='Автор', null=True)
    category = models.TextField(choices=CATEGORY, null=True, blank=True)
    programming_language = models.TextField(choices=PROGRAMMING_LANGUAGES, null=True, blank=True)
    # authors = models.ManyToManyField('persons.Person', related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    # banner = models.CharField(max_length=255)
    # hashtags = models.TextField()
    link_on_code = models.CharField(max_length=255, verbose_name='Ссылка на гитхаб')
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
