# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0011_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='s_class',
            field=models.CharField(max_length=6),
        ),
    ]
