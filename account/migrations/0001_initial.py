# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import account.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.ImageField(verbose_name='تصویر', upload_to='account_extra_images')),
            ],
        ),
        migrations.CreateModel(
            name='AccountLink',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='نام', null=True, blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AccountRole',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Role', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='AccountTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Role', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='BaseAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(verbose_name='username', max_length=30, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True)),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('type', models.CharField(verbose_name='Account Type', choices=[('AD', 'Admin'), ('US', 'User')], default='US', max_length=4)),
                ('phone', models.CharField(verbose_name='Phone', null=True, blank=True, max_length=30)),
                ('im', models.CharField(verbose_name='IM', null=True, blank=True, max_length=255)),
                ('website', models.CharField(verbose_name='Website', null=True, blank=True, max_length=1024)),
            ],
            managers=[
                ('objects', account.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteFilters',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Filter Name', max_length=128)),
                ('query', models.CharField(verbose_name='Filter Query', max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='OtherProject',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='نام', null=True, blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('baseaccount_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='account.BaseAccount', serialize=False, primary_key=True)),
                ('description', models.TextField(verbose_name='توضیحات', null=True, blank=True)),
                ('image', models.ImageField(verbose_name='تصویر', null=True, upload_to='account_image')),
            ],
            bases=('account.baseaccount',),
            managers=[
                ('objects', account.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='RelationAccount',
            fields=[
                ('baseaccount_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='account.BaseAccount', serialize=False, primary_key=True)),
                ('description', models.TextField(verbose_name='توضیحات', null=True, blank=True)),
            ],
            bases=('account.baseaccount',),
        ),
        migrations.AddField(
            model_name='otherproject',
            name='account',
            field=models.OneToOneField(verbose_name='Account', related_name='projects', to='account.BaseAccount'),
        ),
        migrations.AddField(
            model_name='favoritefilters',
            name='account',
            field=models.ForeignKey(verbose_name='Account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favoritefilters',
            name='filters',
            field=models.ManyToManyField(verbose_name='Filters', to='account.Filter'),
        ),
        migrations.AddField(
            model_name='baseaccount',
            name='follows',
            field=models.ManyToManyField(null=True, related_name='followers', blank=True, to='account.BaseAccount'),
        ),
        migrations.AddField(
            model_name='baseaccount',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', related_name='user_set', to='auth.Group', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True),
        ),
        migrations.AddField(
            model_name='baseaccount',
            name='role',
            field=models.ForeignKey(verbose_name='Role', null=True, to='account.AccountRole', blank=True),
        ),
        migrations.AddField(
            model_name='baseaccount',
            name='team',
            field=models.ForeignKey(verbose_name='Team', null=True, to='account.AccountTeam', blank=True),
        ),
        migrations.AddField(
            model_name='baseaccount',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', related_name='user_set', to='auth.Permission', related_query_name='user', help_text='Specific permissions for this user.', blank=True),
        ),
        migrations.AddField(
            model_name='accountlink',
            name='account',
            field=models.OneToOneField(verbose_name='Account', related_name='links', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accountimage',
            name='account',
            field=models.ForeignKey(verbose_name='Account', related_name='extra_images', to=settings.AUTH_USER_MODEL),
        ),
    ]
