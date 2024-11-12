from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


class SignUpSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value

    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create(name=name, email=email, is_active=True)
        user.set_password(password)
        user.save()

        user.generate_otp()
        return user


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        otp_code = data.get('otp_code')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("No user found with this email")

        if not user.is_otp_valid(otp_code):
            raise serializers.ValidationError("Invalid or expired OTP code")

        data['user'] = user
        return data

    def update(self, instance, validated_data):
        instance.is_active = True
        instance.otp_code = None
        instance.otp_expires = None
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Incorrect email or password")
        if not user.is_active:
            raise serializers.ValidationError("User is inactive")

        return {'user': user}

    def create(self, validated_data):
        user = validated_data['user']
        token = AccessToken.for_user(user)
        return {'token': str(token)}
