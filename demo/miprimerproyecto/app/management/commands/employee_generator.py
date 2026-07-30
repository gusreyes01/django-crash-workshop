import secrets

from app.models import Employee, Role
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


@transaction.atomic
def create_employee(index: int, role: Role) -> Employee:
    """Create a synthetic workshop employee without a shared password."""
    token = secrets.token_hex(4)
    email = f"workshop-{index}-{token}@example.invalid"
    user = get_user_model().objects.create_user(
        username=email,
        first_name=f"Workshop {index}",
        last_name="Employee",
        email=email,
    )
    user.set_unusable_password()
    user.save(update_fields=["password"])
    return Employee.objects.create(
        user=user,
        salary=3000 + ((index * 500) % 9000),
        role=role,
    )


def create_n_random_employees(number_of_employees: int) -> list[Employee]:
    """Create the requested number of synthetic employees."""
    role, _ = Role.objects.get_or_create(name="1")
    return [create_employee(index, role) for index in range(number_of_employees)]


class Command(BaseCommand):
    help = "Create synthetic employees for the workshop"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, required=True)

    def handle(self, *args, **options):
        number = options["number"]
        if not 1 <= number <= 1000:
            raise CommandError("--number must be between 1 and 1000")
        employees = create_n_random_employees(number)
        self.stdout.write(self.style.SUCCESS(f"Created {len(employees)} employees"))
