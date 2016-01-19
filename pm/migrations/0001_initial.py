# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=255, db_index=True)),
                ('_prev_title', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, populate_from='title', editable=False)),
                ('summary', models.TextField(null=True, verbose_name='Summary', blank=True)),
                ('entry_date', models.DateTimeField(verbose_name='Create Date', auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=255, db_index=True)),
                ('_prev_title', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, populate_from='title', editable=False)),
                ('effort', models.CharField(null=True, verbose_name='Effort', max_length=128, blank=True)),
                ('effort_calc', models.PositiveIntegerField(null=True, verbose_name='Effort Calculated', editable=False, blank=True)),
                ('bug_to_fixed', models.PositiveIntegerField(null=True, verbose_name='Bugs to Fixed', blank=True)),
                ('bug_fixed', models.PositiveIntegerField(null=True, verbose_name='Bugs Fixed', blank=True)),
                ('feature_to_develop', models.PositiveIntegerField(null=True, verbose_name='Feature to Develop', blank=True)),
                ('feature_developed', models.PositiveIntegerField(null=True, verbose_name='Feature Developed', blank=True)),
                ('due_date', models.DateTimeField(null=True, verbose_name='Due Date', blank=True)),
                ('complete_date', models.DateTimeField(null=True, verbose_name='Date Completed', blank=True)),
                ('entry_date', models.DateTimeField(verbose_name='Create Date', auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('responsible', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Responsible', blank=True)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='MilestoneStatus',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('status', models.CharField(verbose_name='Status', max_length=128)),
                ('entry_date', models.DateTimeField(verbose_name='Create Date', auto_now_add=True)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=255, db_index=True)),
                ('_prev_title', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('summary', models.TextField(null=True, verbose_name='Summary', blank=True)),
                ('entry_date', models.DateTimeField(verbose_name='Create Date', auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('responsible', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Responsible', blank=True)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Category Name', max_length=128)),
                ('_prev_name', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('entry_date', models.DateTimeField(verbose_name='Create Date', auto_now_add=True)),
                ('responsible', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Responsible', blank=True)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='ProjectMembership',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='توضیح')),
                ('members', models.ManyToManyField(verbose_name='Members', to=settings.AUTH_USER_MODEL, blank=True)),
                ('project', models.ForeignKey(verbose_name='Project', to='pm.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectVersion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=255, db_index=True)),
                ('_prev_title', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('summary', models.TextField(null=True, verbose_name='Summary', blank=True)),
                ('entry_date', models.DateTimeField(verbose_name='Create Date', auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('category', models.ForeignKey(null=True, to='pm.ProjectCategory', verbose_name='Category', blank=True)),
                ('milestones', models.ManyToManyField(verbose_name='Milestones', to='pm.Milestone', blank=True)),
                ('project', models.ForeignKey(verbose_name='Project', to='pm.Project')),
                ('responsible', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Responsible', blank=True)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='TimeSpend',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='عنوان', max_length=255)),
                ('created_on', models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)),
                ('due_date', models.DateField(null=True, verbose_name='زمان')),
                ('desc', models.TextField(null=True, verbose_name='توضیح')),
                ('time_spend', models.FloatField(null=True, verbose_name='زمان گذاشته شده')),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='assignes', verbose_name='واگذارشده به')),
                ('creator', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='سازنده', blank=True)),
                ('project', models.ForeignKey(null=True, to='pm.Project', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='status',
            field=models.ForeignKey(null=True, to='pm.MilestoneStatus', verbose_name='Status', blank=True),
        ),
        migrations.AddField(
            model_name='board',
            name='project',
            field=models.ForeignKey(verbose_name='Project', to='pm.Project'),
        ),
    ]
