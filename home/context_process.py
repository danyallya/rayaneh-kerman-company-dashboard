# -*- coding:utf-8 -*-
from datetime import date

__author__ = 'M.Y'


def default_context(request):

    today = date.today()
    result = {'today': today}

    return result
