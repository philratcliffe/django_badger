from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('add_employee/', views.EmployeeCreate.as_view()),
]
