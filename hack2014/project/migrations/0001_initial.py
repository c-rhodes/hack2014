# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=32, help_text='The name of the category')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128, help_text='A short name identifying the project')),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='project.Category')),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='projects')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
