# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0016_auto_20180603_1105'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='grade',
            table='stu_grade',
        ),
    ]