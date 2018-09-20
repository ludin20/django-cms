# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-11 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4CardColumnsModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='card_columns_plugin_bootstrap4cardcolumnsmodel', serialize=False, to='cms.CMSPlugin')),
                ('card_columns_sm', models.CharField(blank=True, choices=[('1', '1 Column'), ('2', '2 Columns'), ('3', '3 Columns'), ('4', '4 Columns')], max_length=256, null=True)),
                ('card_columns_md', models.CharField(blank=True, choices=[('1', '1 Column'), ('2', '2 Columns'), ('3', '3 Columns'), ('4', '4 Columns')], max_length=256, null=True)),
                ('card_columns_lg', models.CharField(blank=True, choices=[('1', '1 Column'), ('2', '2 Columns'), ('3', '3 Columns'), ('4', '4 Columns')], max_length=256, null=True)),
                ('card_columns_xl', models.CharField(blank=True, choices=[('1', '1 Column'), ('2', '2 Columns'), ('3', '3 Columns'), ('4', '4 Columns')], max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
