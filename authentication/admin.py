from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'permission', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('permission', 'is_admin',)}),
    )
    # readonly_fields = ('crated_at', 'updated_at')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'permission', 'created_at', 'updated_at')}
         ),
    )
    search_fields = ('email', 'name')
    ordering = ('email', 'name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
