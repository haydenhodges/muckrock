# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-07-07 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0021_remove_jurisdiction_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='jurisdiction.Jurisdiction'),
        ),
    ]
