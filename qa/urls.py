from django.urls import path, include
import django.contrib.auth.urls

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/', include('django.contrib.auth.urls')),
]
