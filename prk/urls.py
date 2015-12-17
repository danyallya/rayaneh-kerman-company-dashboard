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
    url(r'^pm/', include('pm.urls')),
    url(r'^home/$', 'home.views.index', name='index'),
    url(r'^my_idea/$', 'home.views.my_idea', name="my_idea"),
    url(r'^list_idea/$', 'home.views.list_idea', name="list_idea"),
    url(r'^mahsool/$', 'home.views.mahsool', name="mahsool"),
    url(r'^list_mahsool/$', 'home.views.list_mahsool', name="list_mahsool"),
    url(r'^project/$', 'home.views.project', name="project"),

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
