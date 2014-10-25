# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=32, help_text='The name of the category')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
    ]
