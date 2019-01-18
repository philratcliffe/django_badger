from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from rest_framework import viewsets

from .models import Badge
from .models import Employee


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

class BadgeDetail(LoginRequiredMixin, DetailView):
    model = Badge
    fields = ['name']
    success_url = reverse_lazy('badger:badge_list')

class BadgeCreate(LoginRequiredMixin, CreateView):
    model = Badge
    fields = ['name']
    success_url = reverse_lazy('badger:badge_list')


class BadgeUpdate(LoginRequiredMixin, UpdateView):
    model = Badge
    fields = ['name']
    success_url = reverse_lazy('badger:badge_list')

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.has_perm('badger.change_badge'):
            return super(BadgeUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class BadgeDelete(LoginRequiredMixin, DeleteView):
    model = Badge
    success_url = reverse_lazy('badger:badge_list')


class BadgeList(LoginRequiredMixin, ListView):
    model = Badge
    paginate_by = 100
