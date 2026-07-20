from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone

from employees.models import Employee, Salary
from departments.models import Department


@login_required
def home(request):

    # Session (Visit Counter)
    visits = request.session.get("dashboard_visits", 0)
    visits += 1
    request.session["dashboard_visits"] = visits

    request.session["last_visit"] = str(timezone.now())

    # Dashboard Statistics
    total_employees = Employee.objects.count()

    total_departments = Department.objects.count()

    active_employees = Employee.objects.filter(
        is_active=True
    ).count()

    monthly_salary = (
        Salary.objects.aggregate(
            total=Sum("basic_salary")
        )["total"] or 0
    )

    context = {
        "dashboard_visits": visits,
        "total_employees": total_employees,
        "total_departments": total_departments,
        "active_employees": active_employees,
        "monthly_salary": monthly_salary,
    }

    response = render(
        request,
        "dashboard/home.html",
        context,
    )

    if not request.COOKIES.get("visited"):
        response.set_cookie(
            "visited",
            "yes",
            max_age=60 * 60 * 24 * 30,
        )
    
    response.set_cookie(
        "cookie_consent",
        "accepted",
        max_age=60 * 60 * 24 * 365   # 1 year
    )

    return response