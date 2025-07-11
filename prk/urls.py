"""prk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^$', 'home.views.intro', name='intro'),
    url(r'^contact/$', 'home.views.contact', name='intro'),

    url(r'^account/', include('account.urls')),
    url(r'^idea/', include('idea.urls')),
    url(r'^fi/', include('money.urls')),
    url(r'^pm/', include('pm.urls')),
    url(r'^apps/', include('intro.urls')),
    url(r'^home/$', 'home.views.index', name='index'),
    url(r'^my_idea/$', 'home.views.my_idea', name="my_idea"),
    url(r'^mahsool/$', 'home.views.mahsool', name="mahsool"),
    url(r'^list_mahsool/$', 'home.views.list_mahsool', name="list_mahsool"),
    url(r'^work_page/$', 'home.views.work_page', name="work_page"),
    url(r'^work_list/$', 'home.views.work_list', name="work_list"),
    url(r'^project/$', 'home.views.project', name="project"),
    url(r'^account_list/$', 'home.views.account_list', name="account_list"),
    url(r'^account_page/$', 'home.views.account_page', name="account_page"),
    url(r'^post_list/$', 'home.views.post_list', name='post_list'),
    url(r'^post_page/$', 'home.views.post_page', name='post_page'),
    url(r'^talk/$', 'home.views.talk', name='talk'),
    url(r'^my_money/$', 'home.views.my_money', name='my_money'),
    url(r'^resume/$', 'home.views.resume', name='resume'),
    url(r'^blog_list/$', 'home.views.blog_list', name='blog_list'),
    url(r'^blog_page/$', 'home.views.blog_page', name="blog_page"),

    # url(r'^admin/prk_files/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^attachments/', include('attachments.account_urls')),

    # url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),

    # url(r'^articles/comments/', include('django.contrib.comments.account_urls')),

    # url(r'^captcha/', include('captcha.urls')),
    #
    # url(r'^pm/', include('prk.pm.urls')),

]

# urlpatterns += [
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.STATIC_ROOT}),
# ]
#
# urlpatterns += [
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.MEDIA_ROOT}),
# ]
