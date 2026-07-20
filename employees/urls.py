from django.urls import path
from . import views


urlpatterns = [

    # Employee URLs

    path(
        "",
        views.employee_list,
        name="employee_list"
    ),

    path(
        "add/",
        views.employee_create,
        name="employee_create"
    ),

    path(
        "<int:pk>/",
        views.employee_detail,
        name="employee_detail"
    ),

    path(
        "<int:pk>/edit/",
        views.employee_update,
        name="employee_update"
    ),

    path(
        "<int:pk>/delete/",
        views.employee_delete,
        name="employee_delete"
    ),



    # Salary URLs

    path(
        "salary/",
        views.salary_list,
        name="salary_list"
    ),

    path(
        "salary/add/",
        views.salary_create,
        name="salary_create"
    ),

    path(
        "salary/<int:pk>/edit/",
        views.salary_update,
        name="salary_update"
    ),

    path(
        "salary/<int:pk>/delete/",
        views.salary_delete,
        name="salary_delete"
    ),

]