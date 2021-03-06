# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 12:52


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foia', '0019_auto_20160330_2039'),
        ('jurisdiction', '0007_auto_20160805_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_language', models.ManyToManyField(blank=True, related_name='appeals', to='jurisdiction.ExampleAppeal')),
                ('communication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appeals', to='foia.FOIACommunication')),
            ],
        ),
    ]
