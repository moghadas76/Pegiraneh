from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import *
from .models import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeAccessPermission(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    HIERARCHY = {'admin': 1,
                 'Manager': 2,
                 'Supervisor': 3,
                 'Employee': 4
                 }

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if obj.user == request.user:
            return True
        if request.method in permissions.SAFE_METHODS:
            if request.user.groups.exists() and obj.user.groups.exists():
                if self.HIERARCHY[request.user.groups.all()[0].name] < self.HIERARCHY[obj.user.groups.all()[0].name]:
                    return True
                else:
                    return False
            else:
                return False

        # Instafnce must have an attribute named `owner`.
        return False


class EmployeeViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, EmployeeAccessPermission]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


# class EmployeeAccessPermission(permissions.BasePermission):
#     message = 'Access to information is not allowed.'
#
#     def has_permission(self, request, view):
#         pass


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
