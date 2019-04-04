from django.contrib.auth.models import User
from rest_framework import serializers

from app.management.commands.employee_generator import create_employee
from app.models import Employee


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializing all the Employees
    """
    user = UserSerializer()

    def create(self, validated_data):
        employee = create_employee()
        return employee

    class Meta:
        model = Employee
        fields = ('id', 'user', 'salary')
