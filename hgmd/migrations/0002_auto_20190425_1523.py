# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("hgmd", "0001_initial")]

    operations = [
        migrations.AddIndex(
            model_name="hgmdpubliclocus",
            index=models.Index(
                fields=["release", "chromosome", "start"], name="hgmd_hgmdpu_release_27246d_idx"
            ),
        )
    ]
