# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from account.models import AccountRole, AccountTeam, Account, Filter, FavoriteFilters, AccountImage, \
    OtherProject, AccountLink

class AccountImageInline(admin.StackedInline):
    model = AccountImage
    can_delete = False
    verbose_name_plural = u'اطلاعات اکانت اعضای داخلی'


class OtherProjectInline(admin.StackedInline):
    model = OtherProject
    can_delete = False
    verbose_name_plural = u'اطلاعات اکانت اعضای داخلی'


class AccountLinkInline(admin.StackedInline):
    model = AccountLink
    can_delete = False
    verbose_name_plural = u'اطلاعات اکانت اعضای داخلی'


class AccountAdmin(ModelAdmin):
    inlines = (AccountImageInline, OtherProjectInline, AccountLinkInline)


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountTeam)
admin.site.register(AccountRole)
admin.site.register(Filter)
admin.site.register(FavoriteFilters)
