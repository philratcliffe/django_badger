from django.contrib import admin
from .models import Badge
from .models import Employee
from .models import BadgeAwarded

class BadgeAdmin(admin.ModelAdmin):
    exclude = ("slug", )

# Register your models here.
admin.site.register(Badge, BadgeAdmin)
admin.site.register(Employee)
admin.site.register(BadgeAwarded)

