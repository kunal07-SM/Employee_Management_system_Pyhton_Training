from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = "__all__"

        widgets = {

            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "designation": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Designation"
            }),

            "department": forms.Select(attrs={
                "class": "form-select"
            }),

            "salary": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "joining_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

            "profile_picture": forms.FileInput(attrs={
                "class": "form-control"
            }),

            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }
from .models import Salary


class SalaryForm(forms.ModelForm):

    class Meta:

        model = Salary

        fields = [
            "employee",
            "month",
            "year",
            "basic_salary",
            "bonus",
            "deduction",
        ]


        widgets = {

            "employee": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),


            "month": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: July"
                }
            ),


            "year": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),


            "basic_salary": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),


            "bonus": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),


            "deduction": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

        }