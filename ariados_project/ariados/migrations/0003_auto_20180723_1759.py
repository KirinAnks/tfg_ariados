# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-23 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ariados', '0002_auto_20180723_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
