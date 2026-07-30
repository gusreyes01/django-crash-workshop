import logging

from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.extras import send_new_employee_email

logger = logging.getLogger(__name__)


class Role(models.Model):
    ROLE_CHOICES = (
        ("1", "Entry"),
        ("2", "Mid"),
        ("3", "Senior"),
    )
    name = models.CharField(max_length=2, choices=ROLE_CHOICES, unique=True, verbose_name="Nombre")

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self) -> str:
        return self.get_name_display()


class Employee(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name="Usuario")
    salary = models.PositiveIntegerField(verbose_name="Salario")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name="Rol")

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ("user__last_name", "user__first_name")

    def __str__(self) -> str:
        return self.user.get_full_name() or self.user.get_username()

    @property
    def full_name(self) -> str:
        return str(self)

    def as_list_item_dict(self) -> dict[str, int | str]:
        return {"id": self.pk, "name": self.full_name, "salary": self.salary}


@receiver(post_save, sender=Employee, dispatch_uid="employee_welcome_email")
def send_employee_welcome(sender, instance=None, created=False, **kwargs):
    """Send mail only after the employee transaction commits."""
    del sender, kwargs
    if created and instance is not None:
        transaction.on_commit(lambda: send_new_employee_email(instance))
        logger.info("Queued welcome email for employee %s", instance.pk)
