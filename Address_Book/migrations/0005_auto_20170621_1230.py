# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Address_Book', '0004_auto_20170621_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(default=0, max_length=64),
        ),
    ]
