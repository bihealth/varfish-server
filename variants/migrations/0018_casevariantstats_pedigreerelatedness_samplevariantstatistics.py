# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 11:33
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("variants", "0017_distillersubmissionbgjob")]

    operations = [
        migrations.CreateModel(
            name="CaseVariantStats",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "case",
                    models.OneToOneField(
                        help_text="The variant statistics object for this case",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="variant_stats",
                        to="variants.Case",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PedigreeRelatedness",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("sample1", models.CharField(max_length=200)),
                ("sample2", models.CharField(max_length=200)),
                ("het_1_2", models.IntegerField()),
                ("het_1", models.IntegerField()),
                ("het_2", models.IntegerField()),
                ("n_ibs0", models.IntegerField()),
                ("n_ibs1", models.IntegerField()),
                ("n_ibs2", models.IntegerField()),
                (
                    "stats",
                    models.ForeignKey(
                        help_text="Pedigree relatdness information",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pedigree_relatedness",
                        to="variants.CaseVariantStats",
                    ),
                ),
            ],
            options={"ordering": ("sample1", "sample2")},
        ),
        migrations.CreateModel(
            name="SampleVariantStatistics",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("sample_name", models.CharField(max_length=200)),
                ("ontarget_transitions", models.IntegerField()),
                ("ontarget_transversions", models.IntegerField()),
                ("ontarget_snvs", models.IntegerField()),
                ("ontarget_indels", models.IntegerField()),
                ("ontarget_mnvs", models.IntegerField()),
                ("ontarget_effect_counts", django.contrib.postgres.fields.jsonb.JSONField()),
                ("ontarget_indel_sizes", django.contrib.postgres.fields.jsonb.JSONField()),
                ("ontarget_dps", django.contrib.postgres.fields.jsonb.JSONField()),
                (
                    "ontarget_dp_quantiles",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=5
                    ),
                ),
                ("het_ratio", models.FloatField()),
                ("chrx_het_hom", models.FloatField()),
                (
                    "stats",
                    models.ForeignKey(
                        help_text="Single-value variant statistics for one individual",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sample_variant_stats",
                        to="variants.CaseVariantStats",
                    ),
                ),
            ],
            options={"ordering": ("sample_name",)},
        ),
    ]
