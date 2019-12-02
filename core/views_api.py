from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Leave, Employee
from core.serializers import EmployeeSerializer, LeaveSerializer


class EmployeeModelViewSet(ModelViewSet):
    """
    API endpoint that allows employee to be viewed, created, edited and deleted.
    """
    queryset = Employee.objects.all().order_by('-date_created')
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class LeaveModelViewSet(ModelViewSet):
    """
    API endpoint that allows employee leaves to be viewed, created, edited and deleted.
    """
    queryset = Leave.objects.all().order_by('-date_created')
    serializer_class = LeaveSerializer
    lookup_field = 'id'

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        start_date = request.data[
            'start_date'] if 'start_date' in request.data else None
        end_date = request.data[
            'end_date'] if 'end_date' in request.data else None
        if not start_date:
            raise ValidationError(detail="Start-date key is None")

        if not end_date:
            raise ValidationError(detail="End-date key is None")

        if start_date > end_date or start_date == end_date:
            raise ValidationError(
                detail="End-date must be greater than Start-date")

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
