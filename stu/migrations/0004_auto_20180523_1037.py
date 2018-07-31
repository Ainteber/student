# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-23 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0003_auto_20180515_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_image', models.ImageField(null=True, upload_to='upload')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='i_image',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='s',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stu.Student'),
        ),
    ]
