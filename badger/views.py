from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Employee

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']
    success_url = '/admin'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']
    success_url = '/admin'

class EmployeeList(ListView):
    model = Employee
    paginate_by = 100
