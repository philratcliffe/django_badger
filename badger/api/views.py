from rest_framework import viewsets

from badger.models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-last_name')
    serializer_class = EmployeeSerializer


