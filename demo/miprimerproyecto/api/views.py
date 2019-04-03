from django.http import JsonResponse

# Create your views here.
from api.decorators import http_basic_auth
from app.models import Employee


@http_basic_auth
def employee_list_api(request):
    employees_list = [x.as_list_item_dict() for x in Employee.objects.all()]
    return JsonResponse(employees_list, safe=False)

def employee_create_api(request):
    pass
