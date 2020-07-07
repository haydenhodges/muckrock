# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-07-07 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0020_auto_20191007_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcommunication',
            name='from_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='from_emails', to='communication.EmailAddress'),
        ),
        migrations.AlterField(
            model_name='emailerror',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='errors', to='communication.EmailAddress'),
        ),
        migrations.AlterField(
            model_name='emailopen',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opens', to='communication.EmailAddress'),
        ),
        migrations.AlterField(
            model_name='faxcommunication',
            name='to_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='faxes', to='communication.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='faxerror',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='errors', to='communication.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='portalcommunication',
            name='portal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='communications', to='portal.Portal'),
        ),
    ]
