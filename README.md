# Django crash workshop

Spanish-language workshop material paired with a working employee-management
demo. The demo covers Django models, forms, authentication, administration,
management commands, email hooks, and a Django REST Framework API.

The application has been updated to Django 6 and Python 3.12. Secrets and host
configuration come from the environment, API endpoints require staff access,
passwords use Django's password validators and hashers, and email is scheduled
only after the employee transaction commits.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
export DJANGO_SECRET_KEY=replace-me
cd demo/miprimerproyecto
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Create synthetic workshop records without assigning shared passwords:

```bash
python manage.py employee_generator --number 10
```

## Test and lint

Run from the repository root:

```bash
python -m ruff check demo/miprimerproyecto
python -m pytest
python demo/miprimerproyecto/manage.py check --deploy
```

## Architecture

- `app/`: employee domain, HTML forms/views, admin, and commands
- `api/`: staff-only REST serializers and endpoints
- `miprimerproyecto/`: environment-driven project settings and routing
- `ejercicios/`: workshop exercises
- `doc/`: workshop slide deck

CI verifies linting, migrations, tests with coverage, deployment checks,
dependency consistency, and vulnerability auditing on each push and pull request.
