from django.urls import include
from django.urls import path
from . import views

app_name = 'badger'

urlpatterns = [
    path('employee_create/', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employee_update/<int:pk>/', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employees_list/', views.EmployeeList.as_view(), name='employees_list'),
]
