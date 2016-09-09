# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-23 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_cable_ip',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_postation',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_wireless_ip',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
