# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-04 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_journey_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]