from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = (
        "id",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "otp_code",
    )
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "id")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "otp_code",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser"),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
