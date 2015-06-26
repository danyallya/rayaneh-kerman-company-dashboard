# -*- coding:utf-8 -*-
from django.contrib import admin
from prk.financial.models import Income, Payment
from prk.utils.admin import HardModelAdmin

__author__ = 'M.Y'

admin.site.register(Income, HardModelAdmin)
admin.site.register(Payment, HardModelAdmin)
