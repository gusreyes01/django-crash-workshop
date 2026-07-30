from django.urls import path

from app.views import employee_create, employee_detail, employee_list

urlpatterns = [
    path("create/", employee_create, name="employee_create"),
    path("list/", employee_list, name="employee_list"),
    path("detail/<int:employee_id>/", employee_detail, name="employee_detail"),
]
