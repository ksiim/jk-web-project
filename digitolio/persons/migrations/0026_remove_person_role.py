# Generated by Django 5.0.3 on 2024-06-18 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0025_alter_person_profile_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='role',
        ),
    ]