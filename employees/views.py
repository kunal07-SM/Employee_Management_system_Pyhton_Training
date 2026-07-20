from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeeForm
from .models import Employee

from .models import Salary
from .forms import SalaryForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from departments.models import Department
from .models import Employee


def employee_list(request):

    employees = Employee.objects.select_related(
        "department"
    )


    # Search

    search = request.GET.get("search")

    if search:

        employees = employees.filter(

            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search) |
            Q(designation__icontains=search)

        )



    # Department Filter

    department = request.GET.get("department")

    if department:

        employees = employees.filter(
            department_id=department
        )



    # Salary Filter

    min_salary = request.GET.get("min_salary")

    max_salary = request.GET.get("max_salary")


    if min_salary:

        employees = employees.filter(
            salary__gte=min_salary
        )


    if max_salary:

        employees = employees.filter(
            salary__lte=max_salary
        )



    # Active Status Filter

    status = request.GET.get("status")


    if status == "active":

        employees = employees.filter(
            is_active=True
        )


    elif status == "inactive":

        employees = employees.filter(
            is_active=False
        )



    # Ordering

    order = request.GET.get(
        "order",
        "first_name"
    )


    employees = employees.order_by(order)



    # Pagination

    paginator = Paginator(
        employees,
        10
    )


    page = request.GET.get("page")


    employees = paginator.get_page(page)



    departments = Department.objects.all()



    context = {

        "employees": employees,

        "departments": departments,

        "search": search,

    }


    return render(
        request,
        "employees/employee_list.html",
        context
    )


def employee_create(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("employee_list")

    else:
        form = EmployeeForm()

    return render(request,
                  "employees/employee_form.html",
                  {"form": form})


def employee_detail(request, pk):

    employee = get_object_or_404(
        Employee.objects.select_related("department"),
        pk=pk
    )

    return render(
        request,
        "employees/employee_detail.html",
        {"employee": employee},
    )


def employee_update(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee,
        )

        if form.is_valid():
            form.save()
            return redirect("employee_list")

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        "employees/employee_form.html",
        {"form": form},
    )


def employee_delete(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")

    return render(
        request,
        "employees/employee_confirm_delete.html",
        {"employee": employee},
    )

def salary_list(request):

    salaries = Salary.objects.select_related(
        "employee"
    )


    return render(
        request,
        "employees/salary_list.html",
        {
            "salaries": salaries
        }
    )



def salary_create(request):

    if request.method == "POST":

        form = SalaryForm(
            request.POST
        )


        if form.is_valid():

            form.save()

            return redirect(
                "salary_list"
            )


    else:

        form = SalaryForm()



    return render(
        request,
        "employees/salary_form.html",
        {
            "form": form
        }
    )



def salary_update(request, pk):

    salary = get_object_or_404(
        Salary,
        pk=pk
    )


    if request.method == "POST":

        form = SalaryForm(
            request.POST,
            instance=salary
        )


        if form.is_valid():

            form.save()

            return redirect(
                "salary_list"
            )


    else:

        form = SalaryForm(
            instance=salary
        )


    return render(
        request,
        "employees/salary_form.html",
        {
            "form": form
        }
    )



def salary_delete(request, pk):

    salary = get_object_or_404(
        Salary,
        pk=pk
    )


    if request.method == "POST":

        salary.delete()

        return redirect(
            "salary_list"
        )


    return render(
        request,
        "employees/salary_confirm_delete.html",
        {
            "salary": salary
        }
    )