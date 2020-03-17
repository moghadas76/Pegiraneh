from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.validators import UniqueValidator

from .models import Employee, Issue
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = User(username=validated_data['username'], email=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            # import pdb;
            # pdb.set_trace()
            return user
        except ValueError as value_error:
            raise value_error


class IssueSerializer(ModelSerializer):
    responder = CharField(source='responder.name', read_only=True)
    issuer = CharField(source='issuer.name', read_only=True)

    class Meta:
        model = Issue
        fields = ['title', 'progress', 'time_spent', 'ideal_time', 'last_update', 'created_date', 'deadline',
                  'description', 'status', 'priority', 'responder', 'issuer']


class EmployeeSerializer(ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['user', 'name', 'registeredDate', 'exit_time', 'arrival_time', 'issues']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(
            email=user_data['email'],
            username=user_data['username'],
            password=make_password(user_data['password'])
        )
        return Employee.objects.create(user=user, **validated_data)
