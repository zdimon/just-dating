# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-06 11:47
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20180206_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='current_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.RoomQuiestion', verbose_name='\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0432\u043e\u043f\u0440\u043e\u0441'),
        ),
        migrations.AlterField(
            model_name='room',
            name='json_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='\u0412\u0441\u0435 \u043f\u043e \u043a\u043e\u043c\u043d\u0430\u0442\u0435', verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441\u044b \u0432\u0438\u043a\u0442\u043e\u0440\u0438\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='room',
            name='question_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]