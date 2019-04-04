import logging
from threading import Thread

from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.extras import send_mail_wrapper
from app.logger import EmployeeLogger

logger = logging.getLogger(__name__)


class Role(models.Model):
    ROLE_CHOICES = (
        ('1', 'Entry'),
        ('2', 'Mid'),
        ('3', 'Senior'),
    )
    name = models.CharField(max_length=2, choices=ROLE_CHOICES, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    salary = models.PositiveIntegerField(verbose_name='Salario')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Rol')

    @property
    def get_is_active(self):
        return self.user.is_active

    @property
    def get_full_name(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.user.get_full_name()

    def as_list_item_dict(self):
        return {'id': self.pk, 'name': self.get_full_name, 'salary': self.salary}


# 0. Disparamos una llamada a un post_save desde la clase Employee
@receiver(post_save, sender=Employee, dispatch_uid="post_post_save")
def post_post_save(sender, instance=None, created=False, **kwargs):
    try:
        # 1. Solamente enviamos el correo para nuevos usuarios
        if created:
            EmployeeLogger.log('Starting post save logging...')

            mail_kwargs = {
                'context': {'employee': instance, 'sender': sender},
                'template': 'app/mail/new_employee_mail.html',
                'title': 'New Employee',
                'recipients': ['gusreyes01@gmail.com'],
            }

            # 2. Iniciamos un thread para no detener la petición mientras se envía el correo.
            thr = Thread(target=send_mail_wrapper,
                         kwargs=mail_kwargs)
            thr.start()
    except Exception as e:
        # 2. En caso de error escribimos en el log

        print('Something went wrong: {}'.format(e))
        EmployeeLogger.error(e)
