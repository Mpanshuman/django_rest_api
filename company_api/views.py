from django.shortcuts import render
from .models import Company
from .serializer import CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_companies(request):
    all_companies = Company.objects.all()
    serializer = CompanySerializer(all_companies, many=True)
    return Response(status=200, data=serializer.data)


@api_view(["GET"])
def get_company(request, pk):
    all_companies = Company.objects.get(pk=pk)
    serializer = CompanySerializer(all_companies, many=False)
    return Response(status=200, data=serializer.data)


@api_view(["POST"])
def create_company(request):
    data = request.data
    serializer = CompanySerializer(data=data)
    if not serializer.is_valid():
        return Response(status=400, data=serializer.errors)
    serializer.save()
    return Response(status=200, data=serializer.data)


@api_view(["POST"])
def update_company(request, pk):
    company = Company.objects.get(pk=pk)
    serializer = CompanySerializer(instance=company, data=request.data)
    if not serializer.is_valid():
        return Response(status=400, data=serializer.errors)
    serializer.save()
    return Response(status=200, data="Updated Successfully")


@api_view(["DELETE"])
def delete_company(request, pk):
    company = Company.objects.get(pk=pk)
    company.delete()
    return Response(status=204, data="Company Deleted")


# Create your views here.
