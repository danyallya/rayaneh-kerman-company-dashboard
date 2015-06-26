from django.conf.urls import patterns, url, include
from account.views.account import RegistrationView, UpdateUser


urlpatterns = patterns('',
                       url(r'^register/', RegistrationView.as_view(success_url='/')),
                       url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),
                       url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/account/login/'}),
                       url(r'^update/', UpdateUser.as_view(success_url='/')),
                       url(r'^create/', include('account.account_urls.create', namespace='create')),
                       url(r'^view/', include('account.account_urls.view', namespace='view')),
                       url(r'^delete/', include('account.account_urls.delete', namespace='delete')),
                       url(r'^edit/', include('account.account_urls.edit', namespace='edit')),
)
