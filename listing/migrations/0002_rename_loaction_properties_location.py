# Generated by Django 4.2.2 on 2023-08-04 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties',
            old_name='loaction',
            new_name='location',
        ),
    ]