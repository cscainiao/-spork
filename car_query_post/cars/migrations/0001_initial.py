# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('plate_number', models.CharField(max_length=8, verbose_name='车牌号')),
                ('date', models.DateField(verbose_name='违章日期')),
                ('why', models.CharField(max_length=9999, verbose_name='违章原因')),
                ('mode', models.CharField(max_length=100, verbose_name='处罚方式')),
                ('accept', models.BooleanField(default=0, verbose_name='是否受理')),
            ],
        ),
    ]