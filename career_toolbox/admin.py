from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')


@admin.register(models.ExternalResource)
class ExternalResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
    search_fields = ('title',)


@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('level', 'description_level')
    search_fields = ('level',)


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
    search_fields = ('title',)


@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)


@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('title', 'point')
    search_fields = ('title',)


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(models.KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ('theme', 'description', 'author')
    search_fields = ('theme',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
