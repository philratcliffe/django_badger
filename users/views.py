from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  DetailView
from badger.models import BadgeAwarded

from .models import CustomUser

class UserDetail(LoginRequiredMixin, DetailView):
    model = CustomUser
    fields = ['username', 'emailaddress']

    def get_object(self):
        return self.request.user



