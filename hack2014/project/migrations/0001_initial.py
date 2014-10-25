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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, help_text='The name of the category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, help_text='A short name identifying the project')),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='project.Category')),
                ('participants', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('user', models.ForeignKey(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
