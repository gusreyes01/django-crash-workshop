# models test
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from api.serializers import EmployeeSerializer
from app.management.commands.employee_generator import create_n_random_employees
from app.models import Employee, Role


# Create your tests here.


class BaseViewTestOne(APITestCase):
    client = APIClient()

    def setUp(self):
        # add test data
        role = Role(name='Entry')
        role.save()

        create_n_random_employees(5)


class GetAllEmployeesTestCase(BaseViewTestOne):

    def test_employees_serializer(self):
        """

        Esta prueba asegura que todos los empleados agregados en el setUp method
        existen cuando hacemos la petición a la api /employees

        python manage.py test <nombre_app>
        python manage.py test api

        """
        # hit the API endpoint
        response = self.client.get(
            reverse("employee-list-drf", kwargs={})
        )
        # fetch the data from db
        expected = Employee.objects.all()
        serialized = EmployeeSerializer(expected, many=True)

        self.assertEqual(True, True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

