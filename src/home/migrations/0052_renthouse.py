# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentHouse',
            fields=[
                ('house_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.House')),
            ],
            bases=('home.house',),
        ),
    ]
