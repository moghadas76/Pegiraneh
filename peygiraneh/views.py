from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import *
from .models import *


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
