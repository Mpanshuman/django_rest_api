from django.contrib import admin
from django.urls import path, include
from .views import EmployeeApi, DeviseGenericView, DeviseUpDeleteView

urlpatterns = [
    path("", EmployeeApi.as_view()),
    path("devise/", DeviseGenericView.as_view()),
    path("devise/<int:id>", DeviseGenericView.as_view()),
]
