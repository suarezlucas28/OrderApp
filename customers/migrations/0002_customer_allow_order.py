# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='allow_order',
            field=models.BooleanField(default=True),
        ),
    ]
