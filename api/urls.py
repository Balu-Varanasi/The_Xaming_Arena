from django.conf.urls.defaults import *

from piston.resource import Resource

from The_Xaming_Arena.api.auth import MyAuth
from The_Xaming_Arena.api.handlers import ExamHandler

my_auth = MyAuth()

urlpatterns = patterns('',
    url(r'^login/$', Resource(handler=ExamHandler, authentication=my_auth)),
)
