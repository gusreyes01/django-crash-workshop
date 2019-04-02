from django.contrib import admin

# Register your models here.
from app.models import Role, Employee


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'role', 'salary', 'get_is_active']


admin.site.register(Role, RoleAdmin)
admin.site.register(Employee, EmployeeAdmin)
