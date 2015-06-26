# -*- coding:utf-8 -*-
from django import template

__author__ = 'M.Y'

register = template.Library()


@register.filter
def cls_name(obj):
    return obj.__class__.__name__


@register.filter
def get_range(value):
    return range(value)
