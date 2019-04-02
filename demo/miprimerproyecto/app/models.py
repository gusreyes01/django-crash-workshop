from django.contrib.auth.models import User
from django.core import signals
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.extras import send_mail_wrapper


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
        verbose_name_plural = 'Empleado'

    def __str__(self):
        return self.user.get_full_name()


# method for updating
@receiver(post_save, sender=Employee, dispatch_uid="post_post_save")
def post_post_save(sender, instance, **kwargs):
    send_mail_wrapper('New Employee', 'mail/new_employee_mail.html', instance, [])
