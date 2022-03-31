from django.shortcuts import render
from rest_framework import generics
from .serializers import CreateUserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegisterUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()