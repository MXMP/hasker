from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    header = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateTimeField()


class Question(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField()
    creation_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    right_answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.header


class Tag(models.Model):
    word = models.CharField(max_length=30)
