from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User



class UserSerializer(serializers.Serializer):
  username = serializers.CharField(max_length = 128)
  password = serializers.CharField(max_length = 128, write_only = True)
  email = serializers.EmailField(max_length = 128)

  class Meta:
    model = User
    fields = ['pk', 'username', 'password', 'email']

  def validate(self, attrs):
    if User.objects.filter(username=attrs['username']).exists():
      raise serializers.ValidationError({'username':('Username is not available')})
    
    if User.objects.filter(email=attrs['email']).exists():
      raise serializers.ValidationError({'email':('Email is  alrady in use')})
    return super().validate(attrs)

  def create(self, validated_data):
    return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=68)
  password = serializers.CharField(max_length=68, min_length=6, write_only=True)
  username = serializers.CharField(max_length=68, read_only = True)
  token_access = serializers.CharField(max_length=512, read_only=True)
  token_refresh = serializers.CharField(max_length=512, read_only=True)

  class Meta:
    model = User
    fields = ['email', 'username', 'password', 'token_refresh', 'token_access']

  def validate(self, attrs):
    email = attrs.get('email', '')
    password = attrs.get('password', '')
    try:
      user = User.objects.get(email = email)
    except User.DoesNotExist:
      raise AuthenticationFailed('Invalid credentials')

    user = auth.authenticate(username = user.username, password=password)

    if not user:
      raise AuthenticationFailed('Invalid credentials')

    refresh = RefreshToken.for_user(user)

    return {
      'email': user.email,
      'username':user.username,
      'token_refresh': str(refresh),
      'token_access':str(refresh.access_token)
    }