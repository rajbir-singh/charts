# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-23 05:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160322_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 23, 5, 37, 58, 473697, tzinfo=utc)),
        ),
    ]
