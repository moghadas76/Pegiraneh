# Generated by Django 3.0.4 on 2020-03-11 14:36

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peygiraneh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='arrival_time',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='exit_time',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
