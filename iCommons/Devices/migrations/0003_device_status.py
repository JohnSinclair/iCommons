# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0002_loanrequest_requester'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.CharField(default='In Storage', max_length=100),
            preserve_default=False,
        ),
    ]