from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group  # Import the Group model
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'father_name', 'is_staff', 'get_groups')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'father_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'group', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)

    def get_groups(self, obj):
        return ", ".join([str(group.name) for group in obj.groups.all()])

    get_groups.short_description = 'Group'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)  # Unregister the default GroupAdmin
admin.site.register(Group, GroupAdmin)  # Register the Group model with the customized admin interface
