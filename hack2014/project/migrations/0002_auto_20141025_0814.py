# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
