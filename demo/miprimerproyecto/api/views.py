from app.models import Employee
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api.serializers import EmployeeCreateSerializer, EmployeeSerializer


@api_view(["GET"])
@permission_classes([IsAdminUser])
def employee_list_api(request):
    del request
    employees = Employee.objects.select_related("user", "role")
    data = EmployeeSerializer(employees, many=True).data
    return Response({"profiles": data, "length": len(data)})


class EmployeeInstanceView(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.select_related("user", "role")
    lookup_url_kwarg = "employee_id"
    permission_classes = (IsAdminUser,)


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.select_related("user", "role")
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)


class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer
    permission_classes = (IsAdminUser,)
