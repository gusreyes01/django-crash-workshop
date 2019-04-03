import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from app.models import Employee


class Command(BaseCommand):
    help = 'Export CSV exmployees'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        date_string = datetime.now().strftime('%m-%d-%Y')
        filename = "employees_{}.csv".format(date_string)

        with open(filename, "w") as file:
            writer = csv.writer(file)

            # Iteramos sobre todos los empleados
            employees = Employee.objects.all()
            writer.writerow(['pk', 'name', 'salary'])

            for employee in employees:

                writer.writerow([employee.pk, employee.get_full_name, employee.salary])

            self.stdout.write('Successfully generated CSV Report with name {}'.format(filename))
