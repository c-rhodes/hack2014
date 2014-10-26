# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='address_first',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='address_second',
            field=models.TextField(null=True, blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='address_third',
            field=models.TextField(null=True, blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='city',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='postcode',
            field=models.TextField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
