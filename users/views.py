from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  DetailView
from badger.models import BadgeAwarded

from .models import CustomUser

class UserDetail(LoginRequiredMixin, DetailView):
    model = CustomUser
    fields = ['username', 'emailaddress']

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['badges_awarded'] = BadgeAwarded.user_badges.badges(user=self.request.user)
        return context




