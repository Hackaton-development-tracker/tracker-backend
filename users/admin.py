from django.contrib import admin

from .models import User, UserSkill


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email'
    )
    list_filter = ('is_active', )
    search_fields = ('email', )
    ordering = ('id',)


@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill', 'level')
