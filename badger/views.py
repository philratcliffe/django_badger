from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Employee

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']
    success_url = '/admin'
