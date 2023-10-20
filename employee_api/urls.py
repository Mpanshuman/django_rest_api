from django.contrib import admin
from django.urls import path, include
from .views import EmployeeApi

urlpatterns = [
    path("", EmployeeApi.as_view()),
]
