from rest_framework.serializers import ModelSerializer

from core.models import Employee, Leave


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'user',
            'first_name',
            'last_name',
            'phone_number'
        )


class LeaveSerializer(ModelSerializer):
    class Meta:
        model = Leave
        fields = (
            'employee',
            'status',
            'days_of_leave',
            'start_date',
            'end_date'
        )
