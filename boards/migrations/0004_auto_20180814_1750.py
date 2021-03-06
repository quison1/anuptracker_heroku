# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-14 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_topic_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='topic',
            name='image_address',
            field=models.CharField(default='fallback-img.png', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.CharField(choices=[('Zero', 'Zero'), ('1', '1'), ('2', '2'), ('3-5', '3-5'), ('5-10', '5-10'), ('10+', '10+')], default=0, max_length=15),
        ),
    ]
