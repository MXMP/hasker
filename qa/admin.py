from django.contrib import admin

from .models import Question, Answer, Tag


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('header', 'author', 'pub_date')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('author', 'for_question', 'pub_date')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Tag)
