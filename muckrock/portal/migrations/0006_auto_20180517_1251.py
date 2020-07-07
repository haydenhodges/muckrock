# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-17 16:51

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20171129_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal',
            name='type',
            field=models.CharField(
                choices=[('foiaonline', 'FOIAonline'), ('govqa', 'GovQA'),
                         ('nextrequest',
                          'NextRequest'), ('foiaxpress', 'FOIAXpress'),
                         ('fbi', 'FBI eFOIPA Portal'), ('webform', 'Web Form'),
                         ('other', 'Other')],
                max_length=11
            ),
        ),
    ]
