# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-29 17:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promeds', '0028_auto_20160929_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='billdate',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
        migrations.AlterField(
            model_name='billmed',
            name='billdate',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
        migrations.AlterField(
            model_name='ordertab',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]
