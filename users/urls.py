from django.urls import include
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('user_profile/', views.UserDetail.as_view(), name='user_profile'),
    path('', include('users.api.urls')),
]
