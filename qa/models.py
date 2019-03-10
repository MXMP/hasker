from django.db import models


# TODO: Это вообще зачем? Заюзать стандартную модель
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    # TODO: может придумаем что-то получше?
    avatar = models.CharField(max_length=100, null=True)
    register_date = models.DateTimeField()


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
