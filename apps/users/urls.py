from django.urls import path
from .views import SignUpView, VerifyOTPView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]