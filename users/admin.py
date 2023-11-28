from django.contrib import admin

from .models import User


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email'
    )
    list_filter = ('is_active', )
    search_fields = ('email', )
    ordering = ('id',)


admin.site.register(User, CustomUserAdmin)
