# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-13 08:13
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0151_emailgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='property_cache_stale',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='property_cache_version',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='annualbookingperiodgroup',
            name='letter',
            field=models.FileField(blank=True, max_length=512, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/docker_shared_data/moorings/private-media/'), upload_to='letter/%Y/%m/%d/%H/'),
        ),
    ]
