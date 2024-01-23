from django.contrib import admin
from .models import Question, Choice, VoteResult


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('own',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'department')


@admin.register(VoteResult)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'option')


