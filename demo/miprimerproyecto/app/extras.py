from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_new_employee_email(employee) -> int:
    """Send the welcome email using configured mail settings."""
    html_message = render_to_string(
        "app/mail/new_employee_mail.html",
        {"employee": employee},
    )
    return send_mail(
        "New employee",
        f"Employee {employee} was created.",
        settings.DEFAULT_FROM_EMAIL,
        [employee.user.email],
        html_message=html_message,
        fail_silently=False,
    )
