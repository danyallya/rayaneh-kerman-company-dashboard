# -*- coding:utf-8 -*-
from django import template

from utils.calverter import gregorian_to_jalali


__author__ = 'M.Y'

register = template.Library()


@register.filter
def cls_name(obj):
    return obj.__class__.__name__


@register.filter
def get_range(value):
    return range(value)


@register.filter
def to_jalali(date):
    return gregorian_to_jalali(date)


@register.filter
def to_jalali_rev(date):
    res = gregorian_to_jalali(date)
    splited = res.split('/')
    year = splited[2]
    month = splited[1]
    day = splited[0]
    return "/".join([year, month, day])


@register.filter
def st_date(date):
    if not date:
        return ''
    return '-'.join([str(x) for x in [date.year, date.month, date.day]])
