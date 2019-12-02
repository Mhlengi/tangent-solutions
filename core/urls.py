from django.urls import include, path
from rest_framework import routers

from core.views_api import EmployeeModelViewSet, LeaveModelViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/apply/employee/leave', LeaveModelViewSet)
router.register(r'api/employee', EmployeeModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls',
                 namespace='rest_framework')),
]
