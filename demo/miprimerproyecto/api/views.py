from django.http import JsonResponse

# Create your views here.
from app.models import Employee


def employee_list_api(request):
    employees_list = [x for x in Employee.objects.all()]
    return JsonResponse(employees_list)

def employee_create_api(request):
    pass
