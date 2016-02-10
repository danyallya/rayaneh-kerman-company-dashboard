# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('created_on', models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)),
                ('account_num', models.CharField(max_length=255, blank=True, null=True, verbose_name='شماره حساب')),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='سازنده', null=True)),
            ],
            options={
                'verbose_name': 'حساب',
                'verbose_name_plural': 'حساب ها',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_on', models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)),
                ('pay_type', models.IntegerField(verbose_name='نوع پرداخت', choices=[(1, 'برداشت'), (2, 'واریز')])),
                ('money_type', models.IntegerField(verbose_name='نوع پرداخت', choices=[(1, 'حقوق'), (2, 'تنخواه')])),
                ('desc', models.TextField(verbose_name='توضیحات', blank=True, null=True)),
                ('code', models.CharField(max_length=255, blank=True, null=True, verbose_name='شماره سند')),
                ('amount', models.BigIntegerField(verbose_name='مبلغ(تومان)', default=0)),
                ('date', models.DateField(verbose_name='تاریخ', blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='سازنده', null=True)),
                ('person', models.ForeignKey(related_name='persons', blank=True, to=settings.AUTH_USER_MODEL, verbose_name='شخص', null=True)),
            ],
            options={
                'verbose_name': 'تراکنش',
                'verbose_name_plural': 'تراکنش ها',
            },
        ),
    ]
