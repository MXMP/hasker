from django.urls import path, include
import django.contrib.auth.urls

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/', include('django.contrib.auth.urls')),
    path('<int:pk>/', views.QuestionView.as_view(), name='question_view')
]
