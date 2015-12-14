# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0003_remove_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmembership',
            name='members',
            field=models.ManyToManyField(verbose_name='Members', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='projectversion',
            name='milestones',
            field=models.ManyToManyField(verbose_name='Milestones', to='pm.Milestone', blank=True),
        ),
    ]
