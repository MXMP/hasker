from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import F

from .models import Question
from .forms import SignUpForm


class IndexView(ListView):
    model = Question
    template_name = 'qa/index.html'
    paginate_by = 20

    def get_ordering(self):
        return '-pub_date'


class QuestionView(DetailView):
    model = Question
    template_name = 'qa/question.html'


class AskView(CreateView):
    model = Question
    template_name = 'qa/ask_question.html'
    # TODO: добавить поле для тегов
    fields = ['header', 'text']


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('qa:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
