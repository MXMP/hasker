from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Question


class IndexView(ListView):
    model = Question
    template_name = 'qa/index.html'
    paginate_by = 20

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class QuestionView(DetailView):
    model = Question
    template_name = 'qa/question.html'


def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.add()
    return HttpResponseRedirect(reverse('qa:question_view', args=(question.id,)))
