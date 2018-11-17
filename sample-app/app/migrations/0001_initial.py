# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import gradient_colorfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', gradient_colorfield.fields.GradientColorField(default='linear-gradient(to bottom, #00f260 0%, #0575e6 100%)', max_length=18)),
            ],
        ),
    ]
