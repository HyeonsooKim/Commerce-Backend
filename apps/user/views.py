from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics

class UserCreate(generics.CreateAPIView):
    """
    유저 회원가입 view
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
