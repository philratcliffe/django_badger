from rest_framework import serializers

from badger.models import Badge
from badger.models import Employee

class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = ("id", "name", )


class EmployeeSerializer(serializers.ModelSerializer):
    badges = BadgeSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "badges", "slug" )
        read_only_fields = ('slug',)
