from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import SignUpSerializer, VerifyOTPSerializer, LoginSerializer

User = get_user_model()


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": "OTP sent to your email"},
            status=status.HTTP_201_CREATED
        )


class VerifyOTPView(APIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        user.is_active = True
        user.otp_code = None
        user.otp_expires = None
        user.save()

        token = AccessToken.for_user(user)

        return Response(
            {
                "message": "OTP verified successfully",
                "access_token": str(token)
            },
            status=status.HTTP_200_OK
        )


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token = serializer.create(serializer.validated_data)
        return Response(
            {
                "message": "Login successful",
                "access_token": token['token']
            },
            status=status.HTTP_200_OK
        )
