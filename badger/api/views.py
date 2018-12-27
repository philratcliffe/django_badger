from rest_framework import generics, permissions

from badger.models import Employee
from .serializers import EmployeeSerializer

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('-last_name')
    serializer_class = EmployeeSerializer


