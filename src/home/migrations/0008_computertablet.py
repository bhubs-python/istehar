# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerTablet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
