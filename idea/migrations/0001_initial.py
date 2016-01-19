# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='عنوان', max_length=255)),
                ('created_on', models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)),
                ('brief', models.TextField(null=True, verbose_name='توضیح مختصر', blank=True)),
                ('first_desc', models.TextField(null=True, verbose_name='توضیحات ایده خام', blank=True)),
                ('economic_justification', models.TextField(null=True, verbose_name='توجیه اقتصادی', blank=True)),
                ('creator', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='سازنده', blank=True)),
                ('project', models.ForeignKey(null=True, to='pm.Project', verbose_name='پروژه', blank=True)),
            ],
            options={
                'verbose_name': 'ایده',
                'verbose_name_plural': 'ایده ها',
            },
        ),
        migrations.CreateModel(
            name='IdeaState',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='عنوان', max_length=255)),
            ],
            options={
                'verbose_name': 'وضعیت ایده',
                'verbose_name_plural': 'وضعیت های ایده',
            },
        ),
        migrations.AddField(
            model_name='idea',
            name='state',
            field=models.ForeignKey(null=True, to='idea.IdeaState', verbose_name='وضعیت', blank=True),
        ),
    ]
