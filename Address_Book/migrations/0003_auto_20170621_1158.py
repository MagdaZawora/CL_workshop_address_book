# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Address_Book', '0002_auto_20170621_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]