# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-24 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0082_auto_20180918_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationdecisionpropose',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.Application'),
        ),
        migrations.AlterUniqueTogether(
            name='applicationdecisionpropose',
            unique_together=set([]),
        ),
    ]