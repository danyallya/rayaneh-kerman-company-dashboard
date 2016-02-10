# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

__author__ = 'M.Y'

urlpatterns = patterns(
    'money.views',

    url(r'^$', 'bank_list', name='bank_list'),
    url(r'^page/(?P<bank_id>\d+)/$', 'bank_page', name='bank_page'),

)
