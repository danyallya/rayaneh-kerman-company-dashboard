# -*- coding:utf-8 -*-
from django.contrib import admin

from discussion.models import Discussion, Speech
from utils.admin import HardModelAdmin


__author__ = 'M.Y'

admin.site.register(Discussion, HardModelAdmin)
admin.site.register(Speech, HardModelAdmin)