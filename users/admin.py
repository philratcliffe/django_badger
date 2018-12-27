from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'job_title']

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('job_title', )}),
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = 'Badger Administration'
