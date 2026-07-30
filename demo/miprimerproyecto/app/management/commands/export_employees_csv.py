import csv
from datetime import date

from app.models import Employee
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Export employees as CSV"

    def handle(self, *args, **options):
        filename = f"employees_{date.today().isoformat()}.csv"

        with open(filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            employees = Employee.objects.select_related("user", "role")
            writer.writerow(["pk", "name", "salary"])
            for employee in employees:
                writer.writerow([employee.pk, employee.full_name, employee.salary])
        self.stdout.write(self.style.SUCCESS(f"Generated {filename}"))
