# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

__author__ = 'M.Y'

urlpatterns = patterns(
    'idea.views',
    url(r'^$', 'idea_list', name='idea_list'),
    url(r'^page/(?P<idea_id>\d+)/$', 'idea_page', name='idea_page'),

)
