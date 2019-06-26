# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("frequencies", "0001_initial")]

    operations = [
        migrations.RemoveIndex(model_name="exac", name="frequencies_release_668614_idx"),
        migrations.RemoveIndex(model_name="gnomadexomes", name="frequencies_release_72be93_idx"),
        migrations.RemoveIndex(model_name="gnomadgenomes", name="frequencies_release_952459_idx"),
        migrations.RemoveIndex(model_name="thousandgenomes", name="frequencies_release_e5bf46_idx"),
        migrations.RenameField(model_name="exac", old_name="position", new_name="start"),
        migrations.RenameField(model_name="gnomadexomes", old_name="position", new_name="start"),
        migrations.RenameField(model_name="gnomadgenomes", old_name="position", new_name="start"),
        migrations.RenameField(model_name="thousandgenomes", old_name="position", new_name="start"),
        migrations.AddField(
            model_name="exac",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exac",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gnomadexomes",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gnomadexomes",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gnomadgenomes",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gnomadgenomes",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="thousandgenomes",
            name="bin",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="thousandgenomes",
            name="end",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="exac",
            unique_together=set([("release", "chromosome", "start", "reference", "alternative")]),
        ),
        migrations.AlterUniqueTogether(
            name="gnomadexomes",
            unique_together=set([("release", "chromosome", "start", "reference", "alternative")]),
        ),
        migrations.AlterUniqueTogether(
            name="gnomadgenomes",
            unique_together=set([("release", "chromosome", "start", "reference", "alternative")]),
        ),
        migrations.AlterUniqueTogether(
            name="thousandgenomes",
            unique_together=set([("release", "chromosome", "start", "reference", "alternative")]),
        ),
        migrations.AddIndex(
            model_name="exac",
            index=models.Index(
                fields=["release", "chromosome", "start", "reference", "alternative"],
                name="frequencies_release_d330e5_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="gnomadexomes",
            index=models.Index(
                fields=["release", "chromosome", "start", "reference", "alternative"],
                name="frequencies_release_d5febf_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="gnomadgenomes",
            index=models.Index(
                fields=["release", "chromosome", "start", "reference", "alternative"],
                name="frequencies_release_a0fce9_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="thousandgenomes",
            index=models.Index(
                fields=["release", "chromosome", "start", "reference", "alternative"],
                name="frequencies_release_f3feb8_idx",
            ),
        ),
    ]
