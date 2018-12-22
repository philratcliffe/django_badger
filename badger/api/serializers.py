from rest_framework import serializers

from badger.models import Badge
from badger.models import Employee

class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = ("name", )


class EmployeeSerializer(serializers.ModelSerializer):
    badges = BadgeSerializer(read_only=True, many=True)


    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "badges", "slug" )
        read_only_fields = ('slug',)
