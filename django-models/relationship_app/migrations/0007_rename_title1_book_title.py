# Generated by Django 5.1 on 2024-08-30 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationshipapp', '0006_rename_title_book_title1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title1',
            new_name='title',
        ),
    ]
