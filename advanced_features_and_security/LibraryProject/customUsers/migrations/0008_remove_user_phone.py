# Generated by Django 5.1 on 2024-09-15 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUsers', '0007_remove_user_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
