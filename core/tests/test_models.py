import pytest
from django.contrib.auth.models import User
from model_mommy import mommy

from core.models import Employee, Leave


@pytest.mark.django_db
class TestModelObjectClass:
    def test_leave_apply_model_object_creation(self):
        admin_user = mommy.make(
            User,
            email="admin@gmail.com",
            first_name="John",
            last_name="Smith"
        )
        employee = mommy.make(
            Employee,
            user=admin_user,
            phone_number='+41524204242',
            first_name=admin_user.first_name,
            last_name=admin_user.last_name
        )
        leave = mommy.make(
            Leave,
            employee=employee,
            start_date="2019-04-12",
            end_date="2019-05-12",
        )

        assert leave.end_date == "2019-05-12"
        assert leave.start_date == "2019-04-12"
        assert leave.employee.user == admin_user
        assert employee.employee_number == 'TS00{}'.format(admin_user.id)
