# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_renthouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentPlotLand',
            fields=[
                ('plotland_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.PlotLand')),
            ],
            bases=('home.plotland',),
        ),
    ]
