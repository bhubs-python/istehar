# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-10 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_tvaccessories'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraCamcoder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
