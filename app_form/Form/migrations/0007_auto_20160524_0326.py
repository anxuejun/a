# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0006_auto_20160524_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.SmallIntegerField(choices=[(0, '\u53f0\u5f0f\u673a'), (1, '\u7b14\u8bb0\u672c'), (2, '\u82f9\u679c\u4e00\u4f53\u673a'), (3, '\u670d\u52a1\u5668'), (4, '\u81ea\u5e26\u7b14\u8bb0\u672c')]),
        ),
    ]
