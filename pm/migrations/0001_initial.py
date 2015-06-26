# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=255, db_index=True)),
                ('_prev_title', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', editable=False, unique=True)),
                ('summary', models.TextField(null=True, verbose_name='Summary', blank=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=255, db_index=True)),
                ('_prev_title', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', editable=False, unique=True)),
                ('effort', models.CharField(null=True, verbose_name='Effort', max_length=128, blank=True)),
                ('effort_calc', models.PositiveIntegerField(null=True, verbose_name='Effort Calculated', editable=False, blank=True)),
                ('bug_to_fixed', models.PositiveIntegerField(null=True, verbose_name='Bugs to Fixed', blank=True)),
                ('bug_fixed', models.PositiveIntegerField(null=True, verbose_name='Bugs Fixed', blank=True)),
                ('feature_to_develop', models.PositiveIntegerField(null=True, verbose_name='Feature to Develop', blank=True)),
                ('feature_developed', models.PositiveIntegerField(null=True, verbose_name='Feature Developed', blank=True)),
                ('due_date', models.DateTimeField(null=True, verbose_name='Due Date', blank=True)),
                ('complete_date', models.DateTimeField(null=True, verbose_name='Date Completed', blank=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('responsible', models.ForeignKey(verbose_name='Responsible', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='MilestoneStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(verbose_name='Status', max_length=128)),
                ('entry_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=255, db_index=True)),
                ('_prev_title', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', editable=False, unique=True)),
                ('summary', models.TextField(null=True, verbose_name='Summary', blank=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('responsible', models.ForeignKey(verbose_name='Responsible', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Category Name', max_length=128)),
                ('_prev_name', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('responsible', models.ForeignKey(verbose_name='Responsible', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='ProjectMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('desc', models.TextField(null=True, verbose_name='توضیح')),
                ('members', models.ManyToManyField(null=True, verbose_name='Members', blank=True, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(verbose_name='Project', to='pm.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=255, db_index=True)),
                ('_prev_title', models.CharField(null=True, max_length=128, editable=False, blank=True)),
                ('summary', models.TextField(null=True, verbose_name='Summary', blank=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, null=True, to='pm.ProjectCategory')),
                ('milestones', models.ManyToManyField(null=True, verbose_name='Milestones', blank=True, to='pm.Milestone')),
                ('project', models.ForeignKey(verbose_name='Project', to='pm.Project')),
                ('responsible', models.ForeignKey(verbose_name='Responsible', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-entry_date'],
            },
        ),
        migrations.CreateModel(
            name='TimeSpend',
            fields=[
                ('basemodel_ptr', models.OneToOneField(primary_key=True, to='utils.BaseModel', auto_created=True, serialize=False, parent_link=True)),
                ('desc', models.TextField(null=True, verbose_name='توضیح', blank=True)),
                ('time_spend', models.FloatField(null=True, verbose_name='زمان گذاشته شده')),
                ('account', models.ForeignKey(verbose_name='واگذارشده به', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, to='pm.Project')),
            ],
            bases=('utils.basemodel',),
        ),
        migrations.AddField(
            model_name='milestone',
            name='status',
            field=models.ForeignKey(verbose_name='Status', blank=True, null=True, to='pm.MilestoneStatus'),
        ),
        migrations.AddField(
            model_name='board',
            name='project',
            field=models.ForeignKey(verbose_name='Project', to='pm.Project'),
        ),
    ]
