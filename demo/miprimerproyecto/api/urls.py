from django.urls import path

from api import views

urlpatterns = [
    path("employee/list/", views.employee_list_api, name="employee-list-api"),
    path("employees/", views.EmployeeList.as_view(), name="employee-list-drf"),
    path("employees/create/", views.EmployeeCreate.as_view(), name="employee-create-drf"),
    path(
        "employees/<int:employee_id>/",
        views.EmployeeInstanceView.as_view(),
        name="employee-detail-drf",
    ),
]
