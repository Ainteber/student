# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-14 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stu_create_time',
        ),
        migrations.RemoveField(
            model_name='student',
            name='stu_operate_time',
        ),
    ]