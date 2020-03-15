from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

employee_router = DefaultRouter()
employee_router.register('employee', EmployeeViewSet)

issue_router = DefaultRouter()
issue_router.register('issue', IssueViewSet)

urlpatterns = []
urlpatterns += employee_router.urls
urlpatterns += issue_router.urls
