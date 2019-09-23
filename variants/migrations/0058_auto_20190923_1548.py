# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-23 15:48
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("variants", "0057_auto_20190920_0801")]

    operations = [
        migrations.CreateModel(
            name="CaseAlignmentStats",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("bam_stats", django.contrib.postgres.fields.jsonb.JSONField(default={})),
                (
                    "case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="variants.Case"
                    ),
                ),
                (
                    "variant_set",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="variants.SmallVariantSet"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="importvariantsbgjob",
            name="path_bam_qc",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(help_text="Path to bam-qc TSV file", max_length=4096),
                default=[],
                size=None,
            ),
        ),
        migrations.AddIndex(
            model_name="casealignmentstats",
            index=models.Index(fields=["case"], name="variants_ca_case_id_42432f_idx"),
        ),
    ]
