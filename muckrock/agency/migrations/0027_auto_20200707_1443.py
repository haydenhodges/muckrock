# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-07-07 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0026_auto_20200707_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencyemail',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='communication.EmailAddress'),
        ),
        migrations.AlterField(
            model_name='agencyphone',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='communication.PhoneNumber'),
        ),
    ]
