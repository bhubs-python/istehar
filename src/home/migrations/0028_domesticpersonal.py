# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_eventhospitality'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomesticPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
