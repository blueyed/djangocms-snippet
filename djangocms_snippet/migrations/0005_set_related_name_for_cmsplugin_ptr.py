# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_snippet', '0004_auto_alter_slug_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippetptr',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_snippet_snippetptr', serialize=False, to='cms.CMSPlugin'),
        ),
    ]
