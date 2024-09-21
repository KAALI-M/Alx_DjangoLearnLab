
# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from relationshipapp.forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext_lazy as _






class UserAdmin(BaseUserAdmin):
    # Use the custom forms for creating and changing users
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # Fields to be used in displaying the User model.
    fieldsets = (
        (None, {'fields': ('username',)}),
        (_('Personal info'), {'fields': ('email', 'date_of_birth', 'profile_photo')}),
        (_('Password Change'), {'fields': ('current_password', 'password', 'confirmed_password')}),  # Include password fields
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to be used in creating a new User.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password', 'confirmed_password'),
        }),
    )

    # Fields to be displayed in the list view
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register the custom User model and the custom admin class
admin.site.register(User, UserAdmin)