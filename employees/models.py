from django.db import models
from departments.models import Department


class Employee(models.Model):
    first_name = models.CharField(
        max_length=100,
        db_index=True
    )

    last_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True,
        db_index=True
    )

    phone = models.CharField(
        max_length=15
    )

    designation = models.CharField(
        max_length=100,
        db_index=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees"
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    joining_date = models.DateField()

    profile_picture = models.ImageField(
        upload_to="employees/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["first_name"]

        indexes = [
            models.Index(fields=["first_name"]),
            models.Index(fields=["email"]),
            models.Index(fields=["designation"]),
            models.Index(fields=["salary"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    from django.db import models


class Salary(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="salary_records"
    )


    month = models.CharField(
        max_length=20
    )


    year = models.IntegerField()



    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    bonus = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )


    deduction = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    def net_salary(self):

        return (
            self.basic_salary
            + self.bonus
            - self.deduction
        )



    def __str__(self):

        return (
            f"{self.employee} - "
            f"{self.month} {self.year}"
        )