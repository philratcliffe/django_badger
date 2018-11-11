from django.urls import include
from django.urls import path
from . import views

app_name = 'badger'

urlpatterns = [
    path('add_employee/', views.EmployeeCreate.as_view(), name='add_employee'),
]
