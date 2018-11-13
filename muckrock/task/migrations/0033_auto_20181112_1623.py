# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-12 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foia', '0062_auto_20181112_1623'),
        ('task', '0032_auto_20180713_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPortalTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='task.Task')),
                ('portal_type', models.CharField(choices=[(b'foiaonline', b'FOIAonline'), (b'govqa', b'GovQA'), (b'nextrequest', b'NextRequest'), (b'foiaxpress', b'FOIAXpress'), (b'fbi', b'FBI eFOIPA Portal'), (b'webform', b'Web Form'), (b'other', b'Other')], max_length=11)),
                ('communication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foia.FOIACommunication')),
            ],
            bases=('task.task',),
        ),
        migrations.AlterField(
            model_name='flaggedtask',
            name='category',
            field=models.TextField(blank=True, choices=[(b'move communication', b'A communication ended up on this request inappropriately.'), (b'no response', b"This agency hasn't responded after multiple submissions."), (b'wrong agency', b'The agency has indicated that this request should be directed to another agency.'), (b'missing documents', b'I should have received documents for this request.'), (b'form', b'The agency has asked that you use a form.'), (b'follow-up complaints', b'Agency is complaining about follow-up messages.'), (b'appeal', b'Should I appeal this response?'), (b'proxy', b'The agency denied the request due to an in-state citzenship law.'), (b'contact info changed', b'User supplied contact info.'), (b'no proxy', b'No proxy was available.'), (b'agency update', b'An agency logged in to the site and updated a request.'), (b'agency new email', b'An agency with no primary email set replied via email.'), (b'manual form', b'A request needs a PDF form to be manually filled out to be submitted')]),
        ),
    ]