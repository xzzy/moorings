# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-02 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0068_registeredvessels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mooringareabookingrange',
            name='range_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mooringareabookingrange',
            name='range_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mooringsitebookingrange',
            name='range_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mooringsitebookingrange',
            name='range_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
