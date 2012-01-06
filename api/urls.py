from django.conf.urls.defaults import *

from piston.resource import Resource

from The_Xaming_Arena.api.auth import MyAuth
from The_Xaming_Arena.api.handlers import AuthHandler

my_auth = MyAuth()

urlpatterns = patterns('',
    url(r'^login/$', Resource(handler=SubjectHandler, authentication=my_auth),
)
