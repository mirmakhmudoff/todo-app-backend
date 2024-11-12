from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValidationError("Email address must be entered.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        email = extra_fields.pop("email", None)
        password = extra_fields.pop("password")

        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(email=email, password=password, **extra_fields)
