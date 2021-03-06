import profile

from django.contrib import admin
from django.urls import path, include

from app.views import employee_detail, employee_list, employee_create

urlpatterns = [
    path('create', employee_create, name='employee_create'),
    path('list', employee_list, name='employee_list'),
    path('detail/<pk>', employee_detail, name='employee_detail'),
]
