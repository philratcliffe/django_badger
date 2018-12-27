from django.urls import include
from django.urls import path


from . import views

app_name = 'users'

urlpatterns = [
    path('user_detail/', views.UserDetail.as_view(), name='user_detail'),
    path('', include('users.api.urls')),
]
