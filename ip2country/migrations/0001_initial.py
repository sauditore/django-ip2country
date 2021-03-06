# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_from', models.PositiveIntegerField(db_index=True, default=0)),
                ('ip_to', models.PositiveIntegerField(db_index=True, default=0)),
                ('country_code', models.CharField(max_length=2)),
                ('country_name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'ip_location',
            },
        ),
    ]
