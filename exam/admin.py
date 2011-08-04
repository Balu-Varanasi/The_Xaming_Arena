from The_Xaming_Arena.exam.models import Answer,Question, Subject,SubmittedAnswers, Exam, ExamIdClass,CorrectAnswers
from django.contrib import admin

admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Answer)
admin.site.register(SubmittedAnswers)
admin.site.register(Exam)
admin.site.register(ExamIdClass)
admin.site.register(CorrectAnswers)
