# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-18 03:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0003_auto_20180611_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='tenure',
        ),
    ]
