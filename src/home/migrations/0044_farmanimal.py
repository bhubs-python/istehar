# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
