# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-17 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0002_auto_20161017_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ic',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='Data Modified'),
        ),
    ]
