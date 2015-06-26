# -*- coding:utf-8 -*-
from django.contrib import admin

from prk.product.models import Product
from prk.utils.admin import HardModelAdmin


__author__ = 'M.Y'

admin.site.register(Product, HardModelAdmin)