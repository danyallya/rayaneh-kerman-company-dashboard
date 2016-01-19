# -*- coding:utf-8 -*-
from django.contrib import admin

from idea.models import Idea
from utils.admin import HardModelAdmin

__author__ = 'M.Y'

admin.site.register(Idea, HardModelAdmin)
