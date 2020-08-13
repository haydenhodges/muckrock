# Generated by Django 2.2.15 on 2020-08-04 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0022_auto_20200707_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(_negated=True, level='l'), null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='jurisdiction.Jurisdiction'),
        ),
    ]