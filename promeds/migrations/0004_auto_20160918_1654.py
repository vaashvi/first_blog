# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-18 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promeds', '0003_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicines',
            old_name='sub_category',
            new_name='sub_categoryname',
        ),
        migrations.AddField(
            model_name='medicines',
            name='sub_categoryno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
