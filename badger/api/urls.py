from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

from rest_framework import routers

from . import views


# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = [
    path('employee/api/', views.EmployeeList.as_view())
]
