# -*- coding:utf-8 -*-
from django.contrib import admin

from prk.discussion.models import Discussion, Speech
from prk.utils.admin import HardModelAdmin


__author__ = 'M.Y'

admin.site.register(Discussion, HardModelAdmin)
admin.site.register(Speech, HardModelAdmin)