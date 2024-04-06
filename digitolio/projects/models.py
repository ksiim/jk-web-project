from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    authors = models.ManyToManyField('persons.Person', related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner = models.CharField(max_length=255)
    hashtags = models.TextField()
    link_on_code = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title