from .base import *  # noqa

ALLOWED_HOSTS = ["*"]
DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

# INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405

# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405

INSTALLED_APPS += ["rest_framework"]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
}

AUTH_USER_MODEL = 'users.User'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


# CORS_ALLOWED_ORIGINS = [
#     "https://api.mirmakhmudoff.uz",
#     "http://147.45.132.15:1123",
#     "https://test-ten-rust-71.vercel.app"
# ]

# CORS_ALLOW_CREDENTIALS = True  # Allows cookies and other credentials with CORS

# # Allowed CORS Headers
# CORS_ALLOW_HEADERS = [
#     'authorization',
#     'content-type',
# ]

# # Allowed HTTP Methods for CORS
# CORS_ALLOW_METHODS = [
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# ]

CORS_ALLOW_ALL_ORIGINS = True

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    "https://api.mirmakhmudoff.uz",
    "http://147.45.132.15:1123",
    "https://test-ten-rust-71.vercel.app"
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True