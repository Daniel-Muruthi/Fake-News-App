# Generated by Django 5.0.4 on 2024-05-04 12:47

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detectorapi', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None, unique=True),
        ),
    ]
