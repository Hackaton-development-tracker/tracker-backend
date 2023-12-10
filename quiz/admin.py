from django.contrib import admin

from .models import AnswerTest, QuestionTest


@admin.register(QuestionTest)
class QuestionTestAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'skills',
    )
    search_fields = ('question',)


@admin.register(AnswerTest)
class AnswerTestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'questions',
        'answer',
        'point_answer',
    )
    list_filter = ('questions',)
