from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        ('User Credentials', {'fields': ['email', 'password']}),
        ('Personal Info', {'fields': ['first_name', 'last_name']}),
        ('permissions', {'fields': ['is_admin', 'is_active']}),
    ]
    
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ['email', 'first_name', 'last_name', 'password1', 'password2'],  
            },
        ),
    ]
    
    search_fields = ["email"]
    ordering = ['email', 'id']
    filter_horizontal = []
    
admin.site.register(User, UserModelAdmin)