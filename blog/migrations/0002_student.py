# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-02 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('roll', models.IntegerField()),
            ],
        ),
    ]
