# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import AccountRole, AccountTeam, Account, Filter, FavoriteFilters, AccountImage, \
    OtherProject, AccountLink
from utils.calverter import gregorian_to_jalali


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


class AccountAdmin(UserAdmin):
    inlines = (AccountImageInline, OtherProjectInline, AccountLinkInline)

    ordering = ('-date_joined',)

    list_display = ('username', 'email', 'first_name', 'is_staff', 'get_created_date')

    def get_created_date(self, obj):
        return gregorian_to_jalali(obj.date_joined)

    get_created_date.short_description = u"تاریخ ثبت نام"
    get_created_date.admin_order_field = 'date_joined'


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountTeam)
admin.site.register(AccountRole)
admin.site.register(Filter)
admin.site.register(FavoriteFilters)
