from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "department",
        "designation",
        "salary",
        "is_active",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "designation",
    )

    list_filter = (
        "department",
        "is_active",
    )

    ordering = (
        "first_name",
    )
from .models import Salary


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):

    list_display = (

        "employee",
        "month",
        "year",
        "basic_salary",
        "bonus",
        "deduction",

    )


    list_filter = (

        "month",
        "year",

    )


    search_fields = (

        "employee__first_name",
        "employee__last_name",

    )