# Generated by Django 3.2.9 on 2021-11-09 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_test',
            new_name='id_slug',
        ),
    ]