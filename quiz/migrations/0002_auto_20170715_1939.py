# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question_num',
            field=models.IntegerField(),
        ),
    ]
