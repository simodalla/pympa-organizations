# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paorganizations', '0006_person_cdr_ab_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telephonenumber',
            name='number',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='number'),
        ),
    ]
