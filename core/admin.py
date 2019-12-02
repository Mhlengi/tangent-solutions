from django.contrib import admin

from core.models import Employee, Leave


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "employee_number",
        "phone_number"
    )


class LeaveAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "employee",
        "days_of_leave",
        "status",
    )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Leave, LeaveAdmin)
