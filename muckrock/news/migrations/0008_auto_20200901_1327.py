# Generated by Django 2.2.15 on 2020-09-01 17:27

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20180307_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='news_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='news_photos/%Y/%m/%d'),
        ),
    ]