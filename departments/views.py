from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count, Sum, Avg

from employees.models import Employee, Salary
from .forms import DepartmentForm
from .models import Department


def department_list(request):
    departments = Department.objects.all()

    # Search
    search = request.GET.get("search")
    if search:
        departments = departments.filter(
            Q(department_name__icontains=search)
            | Q(manager_name__icontains=search)
            | Q(location__icontains=search)
        )

    # Ordering
    order = request.GET.get("order", "department_name")
    departments = departments.order_by(order)

    # Pagination
    paginator = Paginator(departments, 10)
    page = request.GET.get("page")
    departments = paginator.get_page(page)

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments,
            "search": search,
            "order": order,
        },
    )


def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm()

    return render(
        request,
        "departments/department_form.html",
        {"form": form},
    )


def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(
        request,
        "departments/department_detail.html",
        {"department": department},
    )


def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)

    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        "departments/department_form.html",
        {"form": form},
    )


def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)

    if request.method == "POST":
        department.delete()
        return redirect("department_list")

    return render(
        request,
        "departments/department_confirm_delete.html",
        {"department": department},
    )

from django.db.models import Count, Sum, Avg
from django.shortcuts import render

from .models import Department
from employees.models import Employee, Salary



def department_dashboard(request):


    departments = Department.objects.annotate(

        employee_count=Count(
            "employees"
        ),

        total_salary=Sum(
            "employees__salary_records__basic_salary"
        ),

        average_salary=Avg(
            "employees__salary_records__basic_salary"
        )

    )



    total_departments = Department.objects.count()



    total_employees = Employee.objects.count()



    total_salary = Salary.objects.aggregate(

        total=Sum("basic_salary")

    )
    
    



    context = {


        "departments": departments,


        "total_departments": total_departments,


        "total_employees": total_employees,


        "total_salary":
            total_salary["total"] or 0,

    }



    return render(

        request,

        "departments/dashboard.html",

        context

    )