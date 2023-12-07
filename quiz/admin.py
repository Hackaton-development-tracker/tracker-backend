from django.contrib import admin
from .models import Test, Question, Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'points')
    search_fields = ['text']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test')
    search_fields = ['text']


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill')
    search_fields = ['title']


admin.site.register(Test, TestAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
