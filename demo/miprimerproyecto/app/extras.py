from django.core.mail import send_mail
from django.template.loader import render_to_string

from app.logger import EmployeeLogger


def send_mail_wrapper(**kwargs):

    html_message = render_to_string(
        kwargs['template'], kwargs['context'])

    send_mail(kwargs['title'],
              '',
              '',
              kwargs['recipients'],
              html_message=html_message,
              fail_silently=False)

    EmployeeLogger.log('Sending new employee email')
