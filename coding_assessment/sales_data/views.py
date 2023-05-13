from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import SalesDataSerializer
from django.contrib.auth import get_user_model
from .models import Sales

# Register API
class SalesDataViewSet(viewsets.ModelViewSet):
    serializer_class = SalesDataSerializer
    queryset = get_user_model().objects.all()



