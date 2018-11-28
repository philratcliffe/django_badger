from django.urls import include
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'badger'

urlpatterns = [
    path('', TemplateView.as_view(template_name='badger/index.html'), name='index'),
    path('employee_create/', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employee_update/<slug:slug>/', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employee_list/', views.EmployeeList.as_view(), name='employee_list'),
    path('badge_create/', views.BadgeCreate.as_view(), name='badge_create'),
    path('badge_update/<int:pk>/', views.BadgeUpdate.as_view(), name='badge_update'),
    path('badge_list/', views.BadgeList.as_view(), name='badge_list'),
]
