# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-27 15:24

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsource', '0017_auto_20180530_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crowdsource',
            options={
                'permissions': ((
                    'form_crowdsource',
                    'Can view and fill out the assignments for this crowdsource'
                ),),
                'verbose_name':
                    'assignment'
            },
        ),
        migrations.AddField(
            model_name='crowdsource',
            name='project_admin',
            field=models.BooleanField(
                default=False,
                help_text=
                'Members of this project will be able to manage this crowdsource as if they were the owner'
            ),
        ),
    ]
