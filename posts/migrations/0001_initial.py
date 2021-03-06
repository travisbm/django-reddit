# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
    ]
