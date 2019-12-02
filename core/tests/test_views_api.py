import pytest
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from rest_framework import status
from rest_framework.utils import json

from core.models import Employee, Leave
from core.views_api import LeaveModelViewSet


@pytest.mark.django_db
class TestApplyEmployeeLeaveApi(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.admin_user = mommy.make(
            User,
            email='admin@gmail.com',
            first_name='John',
            last_name='Smith'
        )
        self.employee = mommy.make(
            Employee,
            user=self.admin_user,
            phone_number='+41524204242',
            first_name=self.admin_user.first_name,
            last_name=self.admin_user.last_name
        )
        self.declined_leave = mommy.make(
            Leave,
            status='Declined',
            employee=self.employee,
            start_date='2019-04-12',
            end_date='2019-05-12',
        )

    def test_get_api_apply_employee_leave_list(self):
        request = self.factory.get('api/v1/apply/employee/leave/')
        view = LeaveModelViewSet.as_view({'get': 'list'})
        response = view(request)

        assert self.declined_leave.employee.id == response.data['results'][0][
            'employee']
        assert response.data['count'] == 1
        assert response.status_code == status.HTTP_200_OK

    def test_get_api_apply_employee_leave_retrieve(self):
        request = self.factory.get(
            'api/v1/apply/employee/leave/{}/'.format(self.declined_leave.id))
        view = LeaveModelViewSet.as_view({'get': 'retrieve'})
        response = view(request, id=self.declined_leave.id)

        assert response.status_code == status.HTTP_200_OK
        assert self.declined_leave.employee.id == response.data['employee']

    def test_delete_api_apply_employee_leave(self):
        request = self.factory.delete(
            'api/v1/apply/employee/leave/{}/'.format(self.declined_leave.id))
        view = LeaveModelViewSet.as_view({'delete': 'destroy'})
        response = view(request, id=self.declined_leave.id)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_update_api_apply_employee_leave(self):
        new_leave = mommy.make(
            Leave,
            status='New',
            employee=self.employee,
            start_date='2019-04-12',
            end_date='2019-05-12',
        )
        content_type = 'application/json'
        data = {
            'employee': self.employee.id,
            'end_date': '2019-07-12',
            'days_of_leave': 15
        }

        request = self.factory.put(
            'api/v1/apply/employee/leave/{}/'.format(new_leave.id),
            json.dumps(data),
            content_type=content_type
        )
        view = LeaveModelViewSet.as_view({'put': 'update'})
        response = view(request, id=new_leave.id)

        assert response.data['employee'] == self.employee.id
        assert response.data['status'] == 'New'
        assert response.data['days_of_leave'] == 15
        assert response.data['end_date'] == '2019-07-12'
        assert response.status_code == status.HTTP_200_OK

    def test_post_api_apply_employee_leave_with_valid_data(self):
        content_type = 'application/json'
        data = {
            'employee': self.employee.id,
            'status': 'Declined',
            'start_date': '2019-04-12',
            'end_date': '2019-07-12',
            'days_of_leave': 15
        }

        request = self.factory.post(
            'api/v1/apply/employee/leave/',
            json.dumps(data),
            content_type=content_type
        )
        view = LeaveModelViewSet.as_view({'post': 'create'})
        response = view(request)

        assert response.data['employee'] == self.employee.id
        assert response.data['status'] == 'Declined'
        assert response.data['days_of_leave'] == 15
        assert response.data['end_date'] == '2019-07-12'
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_api_apply_employee_leave_with_invalid_end_date_data(self):
        content_type = 'application/json'
        data = {
            'employee': self.employee.id,
            'status': 'Declined',
            'start_date': '2019-07-12',
            'end_date': '2019-07-12',
            'days_of_leave': 15
        }

        request: WSGIRequest = self.factory.post(
            'api/v1/apply/employee/leave/',
            json.dumps(data),
            content_type=content_type
        )
        view = LeaveModelViewSet.as_view({'post': 'create'})
        response = view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data[0] == 'End-date must be greater than Start-date'

    def test_post_api_apply_employee_leave_with_wrong_format_start_date(self):
        content_type = 'application/json'
        data = {
            'employee': self.employee.id,
            'status': 'Declined',
            'start_date': '2019-05-34',
            'end_date': '2019-07-12',
            'days_of_leave': 15
        }

        request = self.factory.post(
            'api/v1/apply/employee/leave/',
            json.dumps(data),
            content_type=content_type
        )
        view = LeaveModelViewSet.as_view({'post': 'create'})
        response = view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['start_date'][
                   0] == 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.'  # noqa

    def test_post_api_apply_employee_leave_with_wrong_format_end_date(self):
        content_type = 'application/json'
        data = {
            'employee': self.employee.id,
            'status': 'Declined',
            'start_date': '2019-05-03',
            'end_date': '2019-07-42',
            'days_of_leave': 15
        }

        request = self.factory.post(
            'api/v1/apply/employee/leave/',
            json.dumps(data),
            content_type=content_type
        )
        view = LeaveModelViewSet.as_view({'post': 'create'})
        response = view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['end_date'][
                   0] == 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.'  # noqa

    def test_post_api_leave_with_start_date_greater_than_end_date(self):
        content_type = 'application/json'
        data = {
            'employee': self.employee.id,
            'status': 'Declined',
            'start_date': '2019-09-03',
            'end_date': '2019-07-03',
            'days_of_leave': 15
        }

        request = self.factory.post(
            'api/v1/apply/employee/leave/',
            json.dumps(data),
            content_type=content_type
        )
        view = LeaveModelViewSet.as_view({'post': 'create'})
        response = view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data[0] == 'End-date must be greater than Start-date'
