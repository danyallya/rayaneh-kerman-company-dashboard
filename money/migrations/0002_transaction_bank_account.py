# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bank_account',
            field=models.ForeignKey(related_name='transactions', default=0, to='money.BankAccount'),
            preserve_default=False,
        ),
    ]
