# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timespend',
            name='due_date',
            field=models.DateField(verbose_name='زمان', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', editable=False, blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='timespend',
            name='desc',
            field=models.TextField(verbose_name='توضیح', null=True),
        ),
    ]
