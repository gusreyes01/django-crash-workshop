import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from app.forms import EmployeeCreateForm
from app.models import Employee, Role


@pytest.fixture
def role(db):
    return Role.objects.create(name="1")


@pytest.fixture
def employee(role):
    user = get_user_model().objects.create_user(
        "ada@example.com",
        email="ada@example.com",
        first_name="Ada",
        last_name="Lovelace",
        password="valid-test-password-42",
    )
    return Employee.objects.create(user=user, salary=8000, role=role)


def test_employee_representation(employee):
    assert str(employee) == "Ada Lovelace"
    assert employee.as_list_item_dict() == {
        "id": employee.pk,
        "name": "Ada Lovelace",
        "salary": 8000,
    }


def test_employee_form_rejects_out_of_range_salary(role):
    form = EmployeeCreateForm(
        data={
            "first_name": "Grace",
            "email": "grace@example.com",
            "password": "valid-test-password-42",
            "salary": 1000,
            "role": role.pk,
        },
    )

    assert not form.is_valid()
    assert "between 2000 and 20000" in form.errors["salary"][0]


def test_employee_form_creates_hashed_user(role):
    form = EmployeeCreateForm(
        data={
            "first_name": "Grace",
            "last_name": "Hopper",
            "email": "GRACE@example.com",
            "password": "valid-test-password-42",
            "salary": 9000,
            "role": role.pk,
        },
    )

    assert form.is_valid(), form.errors
    employee = form.save()
    assert employee.user.email == "grace@example.com"
    assert employee.user.check_password("valid-test-password-42")


def test_employee_list_requires_login(client):
    response = client.get(reverse("employee_list"), secure=True)

    assert response.status_code == 302


def test_employee_detail_returns_employee(client, employee):
    client.force_login(employee.user)

    response = client.get(reverse("employee_detail", args=[employee.pk]), secure=True)

    assert response.status_code == 200
    assert b"Ada Lovelace" in response.content
