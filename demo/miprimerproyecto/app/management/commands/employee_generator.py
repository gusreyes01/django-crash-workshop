import random

import names
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app.models import Employee, Role


def create_employee():
    salary = random.randrange(3000, 12000)

    name_list = names.get_full_name().split(' ')
    first_name = name_list[0]
    last_name = name_list[1]

    user = User.objects.create_user(username=first_name + last_name,
                                    first_name=first_name,
                                    last_name=last_name,
                                    email='{}@gmail.com'.format(name_list[0]),
                                    password='somepass')

    employee = Employee(user=user, salary=salary,
                        role=Role.objects.get(pk='1'))

    employee.save()

    return employee


# Refactoring del método crear empleado para poder reutilizarlo
def create_n_random_employees(number_of_employees):
    employees_list = []
    for x in range(number_of_employees):
        try:
            employee = create_employee()
            employees_list.append(employee)
            print('Successfully generated Employee name {}'.format(first_name))


        except Exception as e:
            print('Employee creation failed [{}]'.format(e))
    return employees_list


class Command(BaseCommand):
    '''
        python manage.py employee_generator --number_of_employees=10
    '''
    help = 'Export CSV employees'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number_of_employees',
            dest='number_of_employees',
            help='number_of_employees to create',
        )

    def handle(self, *args, **options):
        number_of_employees = int(options['number_of_employees'])
        create_n_random_employees(number_of_employees)
