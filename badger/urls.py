from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

from rest_framework import routers

from . import views

app_name = 'badger'

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='badger/index.html'),
        name='index'),
    path('', include('badger.api.urls')),
    path(
        'employee_create/',
        views.EmployeeCreate.as_view(),
        name='employee_create'),
    path(
        'employee_detail/<slug:slug>/',
        views.EmployeeDetail.as_view(),
        name='employee_detail'),
    path(
        'employee_update/<slug:slug>/',
        views.EmployeeUpdate.as_view(),
        name='employee_update'),
    path(
        'employee_delete/<slug:slug>/',
        views.EmployeeDelete.as_view(),
        name='employee_delete'),
    path('employee_list/', views.EmployeeList.as_view(), name='employee_list'),
    path('badge_create/', views.BadgeCreate.as_view(), name='badge_create'),
    path(
        'badge_update/<slug:slug>/',
        views.BadgeUpdate.as_view(),
        name='badge_update'),
    path('badge_list/', views.BadgeList.as_view(), name='badge_list'),
]
