import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="app.role",
                verbose_name="Rol",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="salary",
            field=models.PositiveIntegerField(verbose_name="Salario"),
        ),
        migrations.AlterField(
            model_name="role",
            name="name",
            field=models.CharField(
                choices=[("1", "Entry"), ("2", "Mid"), ("3", "Senior")],
                max_length=2,
                unique=True,
                verbose_name="Nombre",
            ),
        ),
        migrations.AlterModelOptions(
            name="employee",
            options={
                "ordering": ("user__last_name", "user__first_name"),
                "verbose_name": "Empleado",
                "verbose_name_plural": "Empleados",
            },
        ),
    ]
