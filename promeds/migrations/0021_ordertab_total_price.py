# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promeds', '0020_auto_20160925_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertab',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
