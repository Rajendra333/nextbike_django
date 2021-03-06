# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0004_user_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='station_id',
            new_name='station',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='bike_id',
            new_name='bike',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='reg_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
