# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-23 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankholiday',
            name='date',
            field=models.DateField(),
        ),
    ]