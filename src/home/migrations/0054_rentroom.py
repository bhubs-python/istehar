# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_rentplotland'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
