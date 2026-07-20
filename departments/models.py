from django.db import models


class Department(models.Model):
    department_name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True
    )

    manager_name = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["department_name"]

        indexes = [
            models.Index(fields=["department_name"]),
            models.Index(fields=["location"]),
        ]

    def __str__(self):
        return self.department_name