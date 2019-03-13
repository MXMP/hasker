from django.urls import path, include

from . import views

app_name = 'qa'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/', include('django.contrib.auth.urls')),
    path('<int:pk>/', views.QuestionView.as_view(), name='question_view'),
    path('<int:question_id>/answer', views.answer_question, name='answer_question'),
    path('<int:question_id>/vote', views.question_vote, name='question_vote'),
]
