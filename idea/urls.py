# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

__author__ = 'M.Y'

urlpatterns = patterns(
    'idea.views',
    url(r'^list/$', 'idea_list', name='idea_list'),
    url(r'^page/$', 'idea_page', name='idea_page'),

)
