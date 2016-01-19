# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20151217_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseaccount',
            name='role',
            field=models.ForeignKey(verbose_name='نقش', null=True, to='account.AccountRole'),
        ),
    ]
