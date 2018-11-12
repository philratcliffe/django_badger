from django.urls import include
from django.urls import path
from . import views

app_name = 'badger'

urlpatterns = [
    path('add_employee/', views.EmployeeCreate.as_view(), name='add_employee'),
    path('update_employee/<int:pk>/', views.EmployeeUpdate.as_view(), name='update_employee'),
    path('list_employees/', views.EmployeeList.as_view(), name='list_employee'),
]
