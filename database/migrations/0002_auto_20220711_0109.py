# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-10 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='waktu',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
