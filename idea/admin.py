# -*- coding:utf-8 -*-
from django.contrib import admin

from prk.idea.models import Idea
from prk.utils.admin import HardModelAdmin


__author__ = 'M.Y'

admin.site.register(Idea, HardModelAdmin)