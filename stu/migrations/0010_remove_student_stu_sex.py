# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 02:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0009_auto_20180530_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stu_sex',
        ),
    ]