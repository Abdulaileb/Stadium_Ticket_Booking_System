from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AdminUser, User
from django.contrib.auth.forms import UserCreationForm
class AdminUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AdminUser
        fields = ('username', 'email', 'full_name')

class AdminUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'full_name', 'designation', 'is_active', 'is_staff', 'is_superuser')
    add_form = AdminUserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'username', 'full_name', 'designation', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

admin.site.register(AdminUser, AdminUserAdmin)

# Customize the admin interface for StudentUser
class UserAdmin(UserAdmin):
    list_display = ('user_email', 'username', 'full_name', 'city', 'gender', 'is_active')
    fieldsets = (
        (None, {'fields': ('user_email', 'username', 'full_name', 'city', 'gender', 'date_of_birth', 'password')}),
        ('Permissions', {'fields': ('is_active',)}),
    )

admin.site.register(User, UserAdmin)
