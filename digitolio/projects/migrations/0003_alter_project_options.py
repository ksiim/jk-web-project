# Generated by Django 5.0.3 on 2024-04-06 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_authors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]
