# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 10:22
from __future__ import unicode_literals

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variants', '0005_load_btree_gin_extension'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='smallvariant',
            index=django.contrib.postgres.indexes.GinIndex(fields=['case_id', 'refseq_effect'], name='variants_sm_case_id_a529e8_gin'),
        ),
        migrations.AddIndex(
            model_name='smallvariant',
            index=django.contrib.postgres.indexes.GinIndex(fields=['case_id', 'ensembl_effect'], name='variants_sm_case_id_071d6b_gin'),
        ),
    ]
