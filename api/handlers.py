from piston.handler import BaseHandler
from The_Xaming_Arena.exam.models import Subject
from The_Xaming_Arena.exam.models import Exam
from The_Xaming_Arena.exam.models import ExamIdClass
from The_Xaming_Arena.exam.models import Answer
from The_Xaming_Arena.exam.models import CorrectAnswers
from The_Xaming_Arena.exam.models import SubmittedAnswers
from The_Xaming_Arena.exam.models import Question

class SubjectHandler(BaseHandler):
    
    allowed_methods = ('GET',)

    model = Subject

    def read(self, request):
        return self.model.objects.all()

class ExamHandler(BaseHandler):
    allowed_methods = ('GET', 'POST',)

    exam_model = Exam
    exam_id_model = ExamIdClass
    answer_model = Answer
    correct_answers_model = CorrectAnswers
    submitted_answers_model = SubmittedAnswers
    question_model = Question

    def post(self, request):

        exam_id = request.POST['exam_id']

        if not self.exam_model.objects.filter(exam_id=exam_id).count() == 0:
            return "Already Submitted the Test"

        e = self.exam_id_model.objects.get(id=exam_id)

        id_list = [e.one, e.two, e.three, e.four, e.five, e.six,
                    e.seven, e.eight, e.nine, e.ten]

        ans_list = []

        for i in range(10):
            a = self.answer_model.objects.get(id=id_list[i])
            ans_list.append(a.answer)

        score = 0

        for i in range(10):
            if ans_list[i] == so[i]:
                score += 1

        sa = self.submitted_answers_model(id_exam=exam_id, one=so[0], two=so[1],
                              three=so[2], four=so[3], five=so[4],
                              six=so[5], seven=so[6], eight=so[7],
                              nine=so[8], ten=so[9])

        sa.save()

        ca = self.correct_answers_model(id_exam=exam_id, one=ans_list[0],
                            two=ans_list[1], three=ans_list[2],
                            four=ans_list[3], five=ans_list[4],
                            six=ans_list[5], seven=ans_list[6],
                            eight=ans_list[7], nine=ans_list[8],
                            ten=ans_list[9]
                            )

        ca.save()

        eu = self.exam(exam_id=exam_id, user=request.user,
                  subject=sub_code, marks_obtained=score)

        eu.save()

        questions = Question.objects.filter(id__in=id_list)

        return score

    def read(self, request):
        
        questions = self.question_model.objects.filter(subject_code=sub_code)
        n = questions.count()

        if n < 10:
            return render_to_response(template_name)

        m = int(math.floor(n / 10))
        position = 0
        temp_list = []
        id_list = []

        for object in self.question_model.objects.filter(subject_code=sub_code):
            temp_list.append(object.id)

        for i in range(10):
            id_list.append(
                        temp_list[int(
                            position + math.floor(random.random() * m)
                            )]
                        )
            position += m

        questions = self.question_model.objects.filter(id__in=id_list)
        id_table = self.exam_id_model(one=id_list[0], two=id_list[1],
                               three=id_list[2], four=id_list[3],
                               five=id_list[4], six=id_list[5],
                               seven=id_list[6], eight=id_list[7],
                               nine=id_list[8], ten=id_list[9])

        id_table.save()
        id_table = self.exam_model.objects.all()
        exam_id = id_table.count()

        return [exam_id, questions,]
