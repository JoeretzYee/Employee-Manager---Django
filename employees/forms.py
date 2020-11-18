from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": True})
    )
    department = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": True})
    )
    position = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": True})
    )
    employee_id = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": True})
    )

    class Meta:
        model = Employee
        fields = ["name", "department", "position", "employee_id"]
