from django.views.generic import ListView, DetailView

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
