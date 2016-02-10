# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

__author__ = 'M.Y'

urlpatterns = patterns(
    'intro.views',
    url(r'^del/$', 'delnev', name='del'),
    url(r'^finite/$', 'finite', name='finite'),

)
