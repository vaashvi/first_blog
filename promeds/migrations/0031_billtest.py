# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-02 11:54
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promeds', '0030_auto_20160930_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='billtest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalprice', models.FloatField(default=0)),
                ('billdate', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('ordertest', models.ManyToManyField(to='promeds.checktest')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
