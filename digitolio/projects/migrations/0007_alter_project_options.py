# Generated by Django 5.0.3 on 2024-05-15 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_at'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]
