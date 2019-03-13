from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import F

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
    question.answer_set.create(content=request.POST['answer_content'], author=request.user)
    return HttpResponseRedirect(reverse('qa:question_view', args=(question.id,)))


def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.POST['question_vote'] == 'up':
        question.votes = F('votes') + 1
        question.save()
    elif request.POST['question_vote'] == 'down':
        question.votes = F('votes') - 1
        question.save()
    return HttpResponseRedirect(reverse('qa:question_view', args=(question.id,)))
