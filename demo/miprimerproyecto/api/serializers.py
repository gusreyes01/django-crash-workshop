from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Employee


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializing all the Employees
    """
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'user', 'salary')