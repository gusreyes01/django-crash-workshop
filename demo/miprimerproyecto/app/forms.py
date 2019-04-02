from django.forms import ModelForm

from app.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Employee

    def __init__(self, *args, **kwargs):
        try:
            self.fields['user'] = kwargs.pop('user')
        except Exception as e:
            print(e)

        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['salary'].widget.attrs['min'] = 2000
        self.fields['salary'].widget.attrs['max'] = 20000
