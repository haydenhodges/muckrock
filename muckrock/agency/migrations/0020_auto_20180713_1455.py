# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-13 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0019_auto_20180515_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencyaddress',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='communication.Address'),
        ),
    ]
