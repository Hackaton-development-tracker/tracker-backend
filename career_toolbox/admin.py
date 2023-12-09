from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')


class ExternalResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
    search_fields = ('title',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
    search_fields = ('title',)


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('title', 'point')
    search_fields = ('title',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ('theme', 'description', 'author')
    search_fields = ('theme',)



model_admin_mapping = {
    models.Project: ProjectAdmin,
    models.ExternalResource: ExternalResourceAdmin,
    models.Course: CourseAdmin,
    models.Specialization: SpecializationAdmin,
    models.Grade: GradeAdmin,
    models.Skill: SkillAdmin,
    models.KnowledgeBase: KnowledgeBaseAdmin,
}

for model, admin_class in model_admin_mapping.items():
    admin.site.register(model, admin_class)
