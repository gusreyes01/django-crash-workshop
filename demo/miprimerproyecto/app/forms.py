from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from app.models import Employee


class EmployeeCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])

    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "email", "password", "salary", "role")
        widgets = {
            "salary": forms.NumberInput(attrs={"min": 2000, "max": 20000}),
        }

    def clean_salary(self):
        salary = self.cleaned_data["salary"]
        if not 2000 <= salary <= 20000:
            raise forms.ValidationError("Salary must be between 2000 and 20000.")
        return salary

    @transaction.atomic
    def save(self, commit=True):
        if not commit:
            raise ValueError("EmployeeCreateForm requires commit=True")
        email = self.cleaned_data["email"].lower()
        user = get_user_model().objects.create_user(
            username=email,
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            email=email,
            password=self.cleaned_data["password"],
        )
        return Employee.objects.create(
            user=user,
            salary=self.cleaned_data["salary"],
            role=self.cleaned_data["role"],
        )
