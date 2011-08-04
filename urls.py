from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'The_Xaming_Arena.views.home', name='home'),
    # url(r'^The_Xaming_Arena/', include('The_Xaming_Arena.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^exam/', include('The_Xaming_Arena.exam.urls')),
    url(r'^accounts/profile/','The_Xaming_Arena.exam.views.home', {'template_name':'accounts/home.html'}),

)
