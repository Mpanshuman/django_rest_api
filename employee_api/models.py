from django.db import models
from company_api.models import Company

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employees"
    )
    salary = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.name


class Devises(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="devises"
    )
    department = models.ManyToManyField(
        Department, related_name="departments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.name
