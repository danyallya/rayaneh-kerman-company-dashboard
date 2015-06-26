# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

__author__ = 'M.Y'

urlpatterns = patterns(
    'account.views',
    url(r'^login/$', 'auth.login', name='login'),
    url(r'^logout/$', 'auth.logout', name='logout'),
    url(r'^signup/$', 'auth.signup', name='signup'),
    url(r'^admin/user_inputs/', 'admin.user_inputs', name="user_inputs"),
    url(r'^profile/$', 'profile.show_profile', name='profile'),
    url(r'^profile/edit$', 'profile.edit_profile', name='edit_profile'),

)
