# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-06 13:00

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsource', '0011_crowdsourcefield_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowdsource',
            name='description',
            field=models.TextField(help_text='May use markdown'),
        ),
    ]
