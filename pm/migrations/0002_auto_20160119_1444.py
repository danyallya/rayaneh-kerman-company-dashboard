# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timespend',
            options={'verbose_name': 'زمان', 'verbose_name_plural': 'زمان ها'},
        ),
    ]
