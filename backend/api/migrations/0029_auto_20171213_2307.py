# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-13 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20171213_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationbalance',
            name='validated_credits',
            field=models.BigIntegerField(),
        ),
    ]
