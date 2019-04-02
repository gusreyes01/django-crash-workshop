from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from app.forms import EmployeeForm
from app.models import Employee, Role


def profile(request):
    vista = 'profile'

    return render(request, 'registration/profile.html', {'vista': vista})


def employee_create(request):
    if request.method == 'GET':
        employee_form = EmployeeForm()

    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            email = request.POST.get('first_name')
            password = request.POST.get('password')

            print('first_name: {}, email: {}, password: {}'.format(first_name, email, password))

            user = User.objects.create_user(username=first_name,
                                            first_name=first_name,
                                            email=email,
                                            password=password)

            employee = Employee(user=user, salary=request.POST.get('salary'),
                                role=Role.objects.get(pk=request.POST.get('role')))

            employee.save()

            messages.success(request, '{}'.format('Usuario guardado exitosamente'))
            return redirect('employee_list')


        except Exception as e:
            print(e)

    return render(request, 'app/employee_create.html', {'employee_form': employee_form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'app/employee_list.html', {"employees": employees})


def employee_detail(request, id=None):
    try:
        employee = get_object_or_404(Employee, pk=id)
        return render(request, 'app/employee_detail.html', {"employee": employee})
    except Exception as e:
        messages.error(request, '{}'.format(e))
        return redirect('employee_list')
