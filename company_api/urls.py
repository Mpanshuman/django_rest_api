from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("all-companies/", get_companies, name="all-companies"),
    path("company/new/", create_company, name="new-company"),
    path("company/update/<int:pk>/", update_company, name="update-company"),
    path("company/delete/<int:pk>/", delete_company, name="delete-company"),
    path("company/<int:pk>/", get_company, name="company"),
]
