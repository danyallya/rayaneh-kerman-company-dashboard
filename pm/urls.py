# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

__author__ = 'M.Y'

urlpatterns = patterns(
    'pm.views',

    url(r'^times/$', 'times', name='times'),
    url(r'^edit_time/(?P<time_id>\d+)/$', 'edit_time', name='edit_time'),
    # url(r'^post/(?P<post_id>\d+)/$', 'post_view', name='post_url'),
    # url(r'^like/(?P<post_id>\w+)/$', 'like', name='like'),


)
