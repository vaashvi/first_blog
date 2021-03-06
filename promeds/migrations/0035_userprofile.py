# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 05:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promeds', '0034_auto_20161003_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=300, null=True)),
                ('blood_group', models.CharField(default='O', max_length=2)),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='profilepic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
