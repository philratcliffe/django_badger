from django.contrib import admin
from .models import Badge
from .models import Employee
from .models import BadgeAwarded
from users.models import CustomUser


class BadgeAdmin(admin.ModelAdmin):
    exclude = ("slug", )


class EmployeeAdmin(admin.ModelAdmin):
    exclude = ("slug", )


class BadgeAwardedAdmin(admin.ModelAdmin):
    list_display = ['user', 'badge']


# Register your models here.
admin.site.register(Badge, BadgeAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(BadgeAwarded, BadgeAwardedAdmin)
