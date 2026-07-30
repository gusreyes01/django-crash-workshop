from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from app.forms import EmployeeCreateForm
from app.models import Employee


@login_required
def profile(request):
    return render(request, "registration/profile.html")


@login_required
def employee_create(request):
    form = EmployeeCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Usuario guardado exitosamente")
        return redirect("employee_list")
    return render(request, "app/employee_create.html", {"employee_form": form})


@login_required
def employee_list(request):
    employees = Employee.objects.select_related("user", "role")
    return render(request, "app/employee_list.html", {"employees": employees})


@login_required
def employee_detail(request, employee_id: int):
    employee = get_object_or_404(
        Employee.objects.select_related("user", "role"),
        pk=employee_id,
    )
    return render(request, "app/employee_detail.html", {"employee": employee})
