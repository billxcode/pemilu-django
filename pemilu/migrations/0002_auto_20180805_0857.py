# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-05 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemilu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nomor_urut',
            field=models.IntegerField(default=0),
        ),
    ]
