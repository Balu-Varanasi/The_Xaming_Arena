from piston.handler import BaseHandler
from The_Xaming_Arena.exam.models import Subject

class SubjectHandler(BaseHandler):
    
    allowed_methods = ('GET',)

    model = Subject

    def read(self, request):
        return self.model.objects.all()


