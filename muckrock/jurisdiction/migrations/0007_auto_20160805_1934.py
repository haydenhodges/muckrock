# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 19:34

# Django
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

# Third Party
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foia', '0019_auto_20160330_2039'),
        ('tags', '0002_remove_tag_user'),
        ('jurisdiction', '0006_jurisdiction_law_analysis'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleAppeal',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('language', models.TextField()),
                (
                    'context',
                    models.TextField(
                        blank=True,
                        help_text=
                        'Under what circumstances is this appeal language most effective?'
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='Exemption',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                (
                    'basis',
                    models.TextField(
                        help_text=
                        'The legal or contextual basis for the exemption.'
                    )
                ),
                (
                    'proper_use',
                    models.TextField(
                        blank=True,
                        help_text=
                        'An editorialized description of cases when the exemption is properly used.'
                    )
                ),
                (
                    'improper_use',
                    models.TextField(
                        blank=True,
                        help_text=
                        'An editorialized description of cases when the exemption is improperly used.'
                    )
                ),
                (
                    'key_citations',
                    models.TextField(
                        blank=True,
                        help_text=
                        'Significant references to the exemption in caselaw or previous appeals.'
                    )
                ),
                (
                    'contributors',
                    models.ManyToManyField(
                        blank=True,
                        related_name='exemptions',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    'jurisdiction',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='exemptions',
                        to='jurisdiction.Jurisdiction'
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='InvokedExemption',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'use_language',
                    models.TextField(
                        blank=True,
                        help_text=
                        'What language did the aguency use to invoke the exemption?'
                    )
                ),
                (
                    'properly_invoked',
                    models.BooleanField(
                        default=True,
                        help_text=
                        'Did the agency properly invoke the exemption to the request?'
                    )
                ),
                (
                    'exemption',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='invokations',
                        to='jurisdiction.Exemption'
                    )
                ),
                (
                    'request',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='foia.FOIARequest'
                    )
                ),
            ],
        ),
        migrations.AddField(
            model_name='exemption',
            name='requests',
            field=models.ManyToManyField(
                blank=True,
                related_name='exemptions',
                through='jurisdiction.InvokedExemption',
                to='foia.FOIARequest'
            ),
        ),
        migrations.AddField(
            model_name='exemption',
            name='tags',
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text='A comma-separated list of tags.',
                through='tags.TaggedItemBase',
                to='tags.Tag',
                verbose_name='Tags'
            ),
        ),
        migrations.AddField(
            model_name='exampleappeal',
            name='exemption',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='example_appeals',
                to='jurisdiction.Exemption'
            ),
        ),
    ]
