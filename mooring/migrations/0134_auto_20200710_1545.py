# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-10 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0133_auto_20200710_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingannualadmission',
            name='annual_booking_period_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mooring.AnnualBookingPeriodGroup'),
        ),
    ]
