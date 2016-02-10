# -*- coding:utf-8 -*-
from django.contrib import admin
from money.models import Transaction
from utils.admin import HardModelAdmin

__author__ = 'M.Y'

admin.site.register(Transaction, HardModelAdmin)
