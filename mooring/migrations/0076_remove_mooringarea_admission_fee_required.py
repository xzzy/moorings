# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-03 03:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0075_delete_overridereason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mooringarea',
            name='admission_fee_required',
        ),
    ]
