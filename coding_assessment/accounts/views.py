from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model

# Register API
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


# Class based view to register user
class RegisterViewSet(viewsets.ModelViewSet):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  queryset = get_user_model().objects.all()
