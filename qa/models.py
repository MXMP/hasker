from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    for_question = models.ForeignKey('qa.Question', on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author} - {self.for_question} - {self.content[:20]}'


class Question(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    right_answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.header


class Tag(models.Model):
    word = models.CharField(max_length=30)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.word
