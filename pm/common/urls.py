from django.conf.urls import patterns, include, url
from prk.pm.common.views import UpdateSiteConfigView
from prk.pm.common.models import MainConfiguration

urlpatterns = patterns('',

    url(r'^',
        UpdateSiteConfigView.as_view(
            model=MainConfiguration,
            success_url='/',
        ),
        name='config'),
)
