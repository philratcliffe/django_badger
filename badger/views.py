from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Employee
from .models import Badge


class EmployeeCreate(CreateView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']
    success_url = reverse_lazy('badger:employee_list')


class EmployeeDetail(DetailView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']
    success_url = reverse_lazy('badger:employee_list')


class EmployeeList(ListView):
    model = Employee
    paginate_by = 100


class BadgeCreate(CreateView):
    model = Badge
    fields = ['name']
    success_url = reverse_lazy('badger:badge_list')


class BadgeUpdate(UpdateView):
    model = Badge
    fields = ['name']
    success_url = reverse_lazy('badger:badge_list')


class BadgeList(ListView):
    model = Badge
    paginate_by = 100
