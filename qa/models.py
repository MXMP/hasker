from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    for_question = models.ForeignKey('qa.Question', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author} - {self.for_question} - {self.content[:20]}'


class Question(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    right_answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('qa:question_view', kwargs={'pk': self.pk})


class Tag(models.Model):
    word = models.CharField(max_length=30)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.word
