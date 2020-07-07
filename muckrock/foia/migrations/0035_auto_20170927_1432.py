# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 14:32

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foia', '0034_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='foiamultirequest',
            name='num_monthly_requests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='foiamultirequest',
            name='num_org_requests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='foiamultirequest',
            name='num_reg_requests',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='foiamultirequest',
            name='status',
            field=models.CharField(
                choices=[('started', 'Draft'), ('submitted', 'Processing'),
                         ('filed', 'Filed')],
                max_length=10
            ),
        ),
    ]
