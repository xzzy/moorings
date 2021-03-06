# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-16 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0156_remove_api_system_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='VesselLicence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_rego', models.CharField(max_length=100)),
                ('licence_id', models.IntegerField(blank=True, null=True)),
                ('licence_type', models.IntegerField(choices=[(1, 'Licence'), (2, 'Authorised User'), (3, 'Annual Admission')], default=None, null=True)),
                ('start_date', models.DateField(default=None, null=True)),
                ('expiry_date', models.DateField(default=None, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Cancelled'), (1, 'Active')], default=1)),
            ],
        ),
    ]
