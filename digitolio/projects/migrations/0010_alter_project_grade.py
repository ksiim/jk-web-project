# Generated by Django 5.0.3 on 2024-06-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_grade_alter_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='grade',
            field=models.IntegerField(null=True, verbose_name='Оценка'),
        ),
    ]
