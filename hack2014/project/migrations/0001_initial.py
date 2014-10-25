# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128, help_text='A short name identifying the project')),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='category.Category')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
                ('user', models.ForeignKey(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
