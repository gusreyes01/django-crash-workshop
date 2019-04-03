from django.urls import path

from api.views import employee_list_api

urlpatterns = [
    path('employee/list', employee_list_api, name='employee_list_api'),
]
