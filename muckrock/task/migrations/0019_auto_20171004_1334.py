# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 13:34

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0018_auto_20161211_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsetask',
            name='predicted_status',
            field=models.CharField(
                blank=True,
                choices=[('started', 'Draft'), ('submitted', 'Processing'),
                         ('ack', 'Awaiting Acknowledgement'),
                         ('processed', 'Awaiting Response'),
                         ('appealing',
                          'Awaiting Appeal'), ('fix', 'Fix Required'),
                         ('payment', 'Payment Required'),
                         ('lawsuit', 'In Litigation'), ('rejected', 'Rejected'),
                         ('no_docs',
                          'No Responsive Documents'), ('done', 'Completed'),
                         ('partial',
                          'Partially Completed'), ('abandoned', 'Withdrawn')],
                max_length=10,
                null=True
            ),
        ),
    ]
