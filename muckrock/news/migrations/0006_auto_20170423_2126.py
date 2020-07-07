# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-23 21:26

# Django
from django.db import migrations, models

# Third Party
import easy_thumbnails.fields

# MuckRock
import muckrock.core.storage


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20161211_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(
                blank=True,
                null=True,
                storage=muckrock.core.storage.QueuedS3DietStorage(),
                upload_to='news_images/%Y/%m/%d'
            ),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(
                storage=muckrock.core.storage.QueuedS3DietStorage(),
                upload_to='news_photos/%Y/%m/%d'
            ),
        ),
    ]
