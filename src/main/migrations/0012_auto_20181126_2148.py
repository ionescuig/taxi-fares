# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20181126_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='journey',
            name='hour',
            field=models.TimeField(),
        ),
    ]
