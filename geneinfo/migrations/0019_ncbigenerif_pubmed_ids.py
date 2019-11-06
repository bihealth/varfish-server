# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 15:52
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("geneinfo", "0018_auto_20191014_1218")]

    operations = [
        migrations.AddField(
            model_name="ncbigenerif",
            name="pubmed_ids",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=16), default=[], size=None
            ),
        )
    ]
