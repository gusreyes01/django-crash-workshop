from django.urls import path
from rest_framework import routers

from api import views
from api.views import employee_list_api

router = routers.DefaultRouter()

urlpatterns = [
    path('employee/list', employee_list_api, name='employee-list-api'),
    # DRF urls
    path('employees/', views.EmployeeList.as_view(), name='employee-list-drf'),
    path('employees/create', views.EmployeeCreate.as_view(), name='employee-create-drf'),
    path('employees/<id>', views.EmployeeInstanceView.as_view(), name='employee-detail-drf'),

]
