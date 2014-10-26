# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, help_text='A short name identifying the project')),
                ('description', models.TextField()),
                ('slug', models.SlugField(null=True, blank=True)),
                ('date', models.DateTimeField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='category.Category')),
                ('participants', models.ManyToManyField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='projects')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
