"""This is the root url configuration file"""

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include
from django.conf.urls.defaults import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('The_Xaming_Arena.api.urls')),
    url(r'^exam/', include('The_Xaming_Arena.exam.urls')),
    url(r'^accounts/profile/', 'The_Xaming_Arena.exam.views.home',
        {'template_name': 'accounts/home.html'}),
)


urlpatterns += patterns(
    'piston.authentication',
    url(r'^oauth/request_token/$','oauth_request_token'),
    url(r'^oauth/authorize/$','oauth_user_auth'),
    url(r'^oauth/access_token/$','oauth_access_token'),
)
      
