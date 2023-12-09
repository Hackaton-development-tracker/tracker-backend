from django.contrib import admin

from .models import User, UserSkill


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email'
    )
    list_filter = ('is_active', )
    search_fields = ('email', )
    ordering = ('id',)


class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level')


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserSkill, UserSkillAdmin)