# Generated by Django 5.0.3 on 2024-06-16 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0021_alter_person_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.group', verbose_name='Группa'),
        ),
    ]