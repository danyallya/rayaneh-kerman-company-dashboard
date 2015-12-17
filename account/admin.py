# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

from account.models import AccountRole, AccountTeam, Account, Filter, FavoriteFilters, AccountImage, \
    OtherProject, AccountLink, AccountPermission
from utils.admin import HardModelAdmin
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
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('role', 'is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    inlines = (AccountImageInline, OtherProjectInline, AccountLinkInline)

    ordering = ('-date_joined',)

    list_display = ('username', 'email', 'first_name', 'is_staff', 'get_created_date')

    def get_created_date(self, obj):
        return gregorian_to_jalali(obj.date_joined)

    get_created_date.short_description = u"تاریخ ثبت نام"
    get_created_date.admin_order_field = 'date_joined'


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountTeam)
admin.site.register(Filter)
admin.site.register(FavoriteFilters)


class AccountPermInline(admin.TabularInline):
    model = AccountPermission
    can_delete = True
    verbose_name_plural = u'اجازه ها'
    extra = 1


class AccountRoleAdmin(HardModelAdmin):
    inlines = (AccountPermInline,)

    list_display = ('name',)


admin.site.register(AccountRole, AccountRoleAdmin)
