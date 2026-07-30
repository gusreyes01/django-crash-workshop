import pytest
from app.models import Employee, Role
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def role(db):
    return Role.objects.create(name="1")


@pytest.fixture
def admin(db):
    return get_user_model().objects.create_superuser(
        "admin@example.com",
        email="admin@example.com",
        password="valid-test-password-42",
    )


@pytest.fixture
def api_client(admin):
    client = APIClient()
    client.force_authenticate(admin)
    return client


def test_employee_api_requires_admin(db):
    response = APIClient().get(reverse("employee-list-drf"), secure=True)

    assert response.status_code in {401, 403}


def test_admin_can_create_and_list_employee(api_client, role):
    create_response = api_client.post(
        reverse("employee-create-drf"),
        {
            "first_name": "Katherine",
            "last_name": "Johnson",
            "email": "katherine@example.com",
            "password": "valid-test-password-42",
            "salary": 10000,
            "role": role.pk,
        },
        format="json",
        secure=True,
    )

    assert create_response.status_code == 201, create_response.data
    list_response = api_client.get(reverse("employee-list-drf"), secure=True)
    assert list_response.status_code == 200
    assert list_response.data[0]["user"]["first_name"] == "Katherine"
    assert Employee.objects.get().user.check_password("valid-test-password-42")


def test_summary_endpoint_returns_length(api_client, role):
    user = get_user_model().objects.create_user(
        "ada@example.com",
        first_name="Ada",
        password="valid-test-password-42",
    )
    Employee.objects.create(user=user, salary=8000, role=role)

    response = api_client.get(reverse("employee-list-api"), secure=True)

    assert response.status_code == 200
    assert response.data["length"] == 1
    assert response.data["profiles"][0]["user"]["first_name"] == "Ada"
