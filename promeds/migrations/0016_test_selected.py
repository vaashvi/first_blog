# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promeds', '0015_order_flago'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='selected',
            field=models.IntegerField(default=0),
        ),
    ]
