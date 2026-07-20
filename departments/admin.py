from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        "department_name",
        "manager_name",
        "location",
        "created_at",
    )

    search_fields = (
        "department_name",
        "manager_name",
        "location",
    )

    ordering = (
        "department_name",
    )

    list_filter = (
        "location",
    )