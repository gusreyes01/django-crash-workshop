from django.contrib import admin

from app.models import Employee, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role", "salary", "is_active")
    list_select_related = ("user", "role")

    @admin.display(boolean=True)
    def is_active(self, obj):
        return obj.user.is_active

    @admin.display(description="Name")
    def full_name(self, obj):
        return obj.full_name
