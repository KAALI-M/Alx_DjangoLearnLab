# Generated by Django 5.1 on 2024-08-31 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationshipapp', '0013_rename_publication_year_author_publication_year1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='publication_year1',
            new_name='publication_year',
        ),
    ]
