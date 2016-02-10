# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pm', '0002_auto_20160119_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='عنوان', max_length=255)),
                ('created_on', models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)),
                ('due_date', models.DateField(verbose_name='زمان انجام', null=True)),
                ('desc', models.TextField(verbose_name='توضیح', null=True)),
                ('progress', models.IntegerField(verbose_name='درصد انجام', default=0)),
                ('account', models.ForeignKey(verbose_name='واگذارشده به', related_name='work_items', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(verbose_name='سازنده', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'کار',
                'verbose_name_plural': 'کارها',
            },
        ),
        migrations.RemoveField(
            model_name='board',
            name='project',
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='status',
        ),
        migrations.RemoveField(
            model_name='projectcategory',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='projectmembership',
            name='members',
        ),
        migrations.RemoveField(
            model_name='projectmembership',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectversion',
            name='category',
        ),
        migrations.RemoveField(
            model_name='projectversion',
            name='milestones',
        ),
        migrations.RemoveField(
            model_name='projectversion',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectversion',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='project',
            name='_prev_title',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Milestone',
        ),
        migrations.DeleteModel(
            name='MilestoneStatus',
        ),
        migrations.DeleteModel(
            name='ProjectCategory',
        ),
        migrations.DeleteModel(
            name='ProjectMembership',
        ),
        migrations.DeleteModel(
            name='ProjectVersion',
        ),
        migrations.AddField(
            model_name='workitem',
            name='project',
            field=models.ForeignKey(blank=True, null=True, to='pm.Project'),
        ),
    ]
