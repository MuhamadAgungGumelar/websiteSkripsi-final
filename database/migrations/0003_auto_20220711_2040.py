# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-11 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20220711_0109'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='PostModel',
        ),
    ]
