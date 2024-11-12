from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    otp_code = models.CharField(max_length=6, null=True, blank=True)
    otp_expires = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        if self.email is not None:
            return self.email

    def generate_otp(self):
        import random
        import datetime
        self.otp_code = str(random.randint(100000, 999999))
        self.otp_expires = timezone.now() + datetime.timedelta(minutes=5)
        self.save()
        self.send_otp_via_email()

    def send_otp_via_email(self):
        subject = 'Your OTP code'
        message = f'Your OTP code is: {self.otp_code}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [self.email]

        send_mail(subject, message, from_email, recipient_list)

    def is_otp_valid(self, otp):
        return self.otp_code == otp and timezone.now() < self.otp_expires

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
