from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import *
from .serializers import *

class UserClientViewSet(viewsets.ModelViewSet):
    serializer_class = UserClientSerializer
    queryset = UserClientModel.objects.all()
