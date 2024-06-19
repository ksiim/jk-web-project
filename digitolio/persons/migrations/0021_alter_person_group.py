# Generated by Django 5.0.3 on 2024-06-16 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0020_alter_person_profile_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='persons.group', verbose_name='Группa'),
        ),
    ]