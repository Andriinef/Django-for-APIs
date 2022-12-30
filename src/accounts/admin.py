from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import CustomUser

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
        "is_active",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": ("age",),
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "email",
                    "age",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


# admin.site.register(CustomUser, CustomUserAdmin)
