# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 15:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("svdbs", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="dbvarsv", name="containing_bins"),
        migrations.RemoveField(model_name="dgvgoldstandardsvs", name="containing_bins"),
        migrations.RemoveField(model_name="dgvsvs", name="containing_bins"),
        migrations.RemoveField(model_name="exaccnv", name="containing_bins"),
        migrations.RemoveField(model_name="gnomadsv", name="containing_bins"),
        migrations.RemoveField(model_name="thousandgenomessv", name="containing_bins"),
    ]
