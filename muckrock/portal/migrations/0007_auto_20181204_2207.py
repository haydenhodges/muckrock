# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-05 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20180517_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal',
            name='type',
            field=models.CharField(choices=[(b'foiaonline', b'FOIAonline'), (b'govqa', b'GovQA'), (b'nextrequest', b'NextRequest'), (b'foiaxpress', b'FOIAXpress'), (b'fbi', b'FBI eFOIPA Portal'), (b'justfoia', b'JustFOIA'), (b'foiadirect', b'FOIA Direct'), (b'webform', b'Web Form'), (b'other', b'Other')], max_length=11),
        ),
    ]
