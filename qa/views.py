from django.views.generic import ListView

from .models import Question


class IndexView(ListView):
    model = Question
    template_name = 'qa/index.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')
