import names
import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app.models import Employee, Role


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


        for x in range(number_of_employees):
            try:
                salary = random.randrange(3000, 12000)

                name_list = names.get_full_name().split(' ')
                first_name = name_list[0]
                last_name = name_list[1]

                user = User.objects.create_user(username=first_name,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email='{}@gmail.com'.format(name_list[0]),
                                                password='somepass')

                employee = Employee(user=user, salary=salary,
                                    role=Role.objects.get(pk='1'))

                employee.save()
                self.stdout.write('Successfully generated Employee name {}'.format(first_name))

            except Exception as e:
                self.stdout.write('Employee creation failed [{}]'.format(e))


