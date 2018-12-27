from rest_framework import generics, permissions
from users.models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]



