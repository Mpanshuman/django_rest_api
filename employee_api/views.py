from django.shortcuts import render, get_list_or_404
from rest_framework.views import APIView
from .models import Employee, Devise, Department
from .serializers import EmployeeSerializer, DepartmentSerializer, DeviseSerializer
from rest_framework.response import Response


# Create your views here.
class EmployeeApi(APIView):
    def get(self, request):
        if request.GET.get("id") != None:
            return Response(
                status=200,
                data=EmployeeSerializer(
                    Employee.objects.get(pk=request.GET.get("id"))
                ).data,
            )
        return Response(
            status=200, data=EmployeeSerializer(Employee.objects.all(), many=True).data
        )

    def post(self, request):
        new_employee = EmployeeSerializer(data=request.data)
        if not new_employee.is_valid():
            return Response(status=400, data="Faied to save employee")

        new_employee.save()
        return Response(status=200, data="Employee Created")

    def patch(self, request):
        try:
            employee = Employee.objects.get(pk=request.GET.get["id"])
            updated_employee = EmployeeSerializer(
                instance=employee, data=request.data, partial=True
            ).save()
            if not updated_employee.is_valid():
                return Response(status=400, data="Faied to update employee")
            return Response(status=200, data="Employee Updated")

        except Exception as e:
            return Response(status=400, data="Failed to get user with provided id")

    def put(self, request):
        pass

    def delete(self, request):
        try:
            employee = Employee.objects.get(pk=request.GET.get("id"))
            employee.delete()
            return Response(status=200, data="Employee Deleted")
        except Exception as e:
            return Response(status=400, data="Failed to get user with provided id")
