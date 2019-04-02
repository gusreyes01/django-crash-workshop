from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_mail_wrapper(title, template, context, recipients):
    html_message = render_to_string(
        template, context)
    send_mail(title,
              '',
              '',
              recipients,
              html_message=html_message,
              fail_silently=False)