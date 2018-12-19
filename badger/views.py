from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from .models import Employee
from .models import Badge
from .serializers import EmployeeSerializer


class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']
    success_url = reverse_lazy('badger:employee_list')


class EmployeeDetail(LoginRequiredMixin, DetailView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'badges']
    success_url = reverse_lazy('badger:employee_list')


class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('badger:employee_list')


class EmployeeList(LoginRequiredMixin, ListView):
    model = Employee
    paginate_by = 100


class BadgeCreate(LoginRequiredMixin, CreateView):
    model = Badge
    fields = ['name']
    success_url = reverse_lazy('badger:badge_list')


class BadgeUpdate(LoginRequiredMixin, UpdateView):
    model = Badge
    fields = ['name']
    success_url = reverse_lazy('badger:badge_list')


class BadgeList(LoginRequiredMixin, ListView):
    model = Badge
    paginate_by = 100


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-last_name')
    serializer_class = EmployeeSerializer


