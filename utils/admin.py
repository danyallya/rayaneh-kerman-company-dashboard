# -*- coding:utf-8 -*-
# from mce_filebrowser.admin import MCEFilebrowserAdmin
from django.contrib.admin import ModelAdmin
from utils.calverter import gregorian_to_jalali, jalali_by_time

__author__ = 'M.Y'


class HardModelAdmin(ModelAdmin):
    def __init__(self, model, admin_site):
        super(HardModelAdmin, self).__init__(model, admin_site)
        self.list_display = list(self.list_display) + ['get_created_date']
        if 'creator' in model._meta.get_all_field_names():
            self.exclude = ('creator',)

    def get_created_date(self, obj):
        return jalali_by_time(obj.created_on)

    get_created_date.short_description = u"تاریخ ایجاد"

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creator = request.user
        obj.save()
