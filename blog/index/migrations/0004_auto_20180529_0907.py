# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_date_pub_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='pub_time',
            field=models.DateTimeField(null=True),
        ),
    ]
