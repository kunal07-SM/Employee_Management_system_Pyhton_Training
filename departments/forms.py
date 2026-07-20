from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = "__all__"

        widgets = {

            "department_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Department Name",
                }
            ),

            "manager_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Manager Name",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Location",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }