# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-31 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("variants", "0049_auto_20190703_1316")]

    operations = [
        migrations.AlterField(
            model_name="case", name="index", field=models.CharField(max_length=512)
        )
    ]
