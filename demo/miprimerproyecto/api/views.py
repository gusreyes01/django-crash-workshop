from django.http import JsonResponse
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from api.decorators import http_basic_auth
from api.serializers import EmployeeSerializer
from app.models import Employee


@http_basic_auth
def employee_list_api(request):
    employees_list = [x.as_list_item_dict() for x in Employee.objects.all()]
    return JsonResponse({'profiles': employees_list, 'length': len(employees_list)})


class EmployeeInstanceView(generics.RetrieveAPIView):
    """
    Regresa un empleado.
    Tambien permite editar y eliminar
    """
    model = Employee
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAdminUser,)


class EmployeeList(generics.ListAPIView):
    """
    Lista todos los empleados.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)

class EmployeeCreate(generics.CreateAPIView):
    pass
