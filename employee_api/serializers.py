from rest_framework import serializers
from .models import Department, Employee, Devise


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ["id", "deleted_at"]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ["id", "deleted_at"]


class DeviseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=True)

    class Meta:
        model = Devise
        exclude = ["id", "deleted_at"]
