# Generated by Django 3.2.9 on 2021-11-07 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='slug_category',
        ),
    ]