# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-17 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20170517_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]