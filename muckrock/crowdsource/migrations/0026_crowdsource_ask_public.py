# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-04 21:13

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsource', '0025_auto_20191209_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='crowdsource',
            name='ask_public',
            field=models.BooleanField(
                default=True,
                help_text=
                'Add a field asking users if we can publically credit them for their response'
            ),
        ),
    ]
