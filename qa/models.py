from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from django.urls import reverse
from django.dispatch import receiver


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_date = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
