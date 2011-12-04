from The_Xaming_Arena.exam.models import Answer
from The_Xaming_Arena.exam.models import Question
from The_Xaming_Arena.exam.models import Subject
from The_Xaming_Arena.exam.models import SubmittedAnswers
from The_Xaming_Arena.exam.models import Exam
from The_Xaming_Arena.exam.models import ExamIdClass
from The_Xaming_Arena.exam.models import CorrectAnswers

from django.contrib import admin


admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Answer)
admin.site.register(SubmittedAnswers)
admin.site.register(Exam)
admin.site.register(ExamIdClass)
admin.site.register(CorrectAnswers)
