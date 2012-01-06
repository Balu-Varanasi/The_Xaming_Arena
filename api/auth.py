from django.contrib.auth.models import AnonymousUser
from piston.authentication import HttpBasicAuthentication

class MyAuth(HttpBasicAuthentication):
    pass
