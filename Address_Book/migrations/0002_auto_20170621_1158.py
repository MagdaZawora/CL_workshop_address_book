# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Address_Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='flat_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
