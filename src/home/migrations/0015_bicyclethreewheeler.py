# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_motorbikescooter'),
    ]

    operations = [
        migrations.CreateModel(
            name='BicycleThreeWheeler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
