# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseaccount',
            name='follows',
            field=models.ManyToManyField(related_name='followers', blank=True, to='account.BaseAccount'),
        ),
    ]
