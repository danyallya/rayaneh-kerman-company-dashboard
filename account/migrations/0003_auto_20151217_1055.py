# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150625_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountPermission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('perm', models.IntegerField(choices=[(1, 'زمان ها!')], verbose_name='ماژول')),
                ('perm_type', models.IntegerField(choices=[(1, 'اجازه شخصی'), (20, 'اجازه کل')], verbose_name='نوع')),
            ],
            options={
                'verbose_name_plural': 'اجازه ها',
                'verbose_name': 'اجازه',
            },
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'کاربران', 'verbose_name': 'کاربر'},
        ),
        migrations.AlterModelOptions(
            name='accountrole',
            options={'verbose_name_plural': 'نقش ها', 'verbose_name': 'نقش'},
        ),
        migrations.AlterField(
            model_name='accountrole',
            name='name',
            field=models.CharField(max_length=128, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='baseaccount',
            name='role',
            field=models.ForeignKey(null=True, verbose_name='نقش', to='account.AccountRole', blank=True),
        ),
        migrations.AddField(
            model_name='accountpermission',
            name='role',
            field=models.ForeignKey(related_name='perms', verbose_name='نقش', to='account.AccountRole'),
        ),
    ]
