# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-24 00:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181123_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='day',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
