from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework.permissions import DjangoModelPermissions
from users.models import CustomUser
from .serializers import CustomUserSerializer


class ReadOnlyAndAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS and request.user.is_authenticated


class CustomUserList(generics.ListCreateAPIView):
    permission_classes = (DjangoModelPermissions| ReadOnlyAndAuthenticated, )

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
