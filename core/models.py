from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='employee'
    )
    employee_number = models.CharField(max_length=250, null=True, blank=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    phone_number = PhoneNumberField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.employee_number = 'TS00{}'.format(self.user.id)
        print(self.user.first_name)
        if self.user.first_name:
            self.first_name = self.user.first_name
        if self.user.last_name:
            self.last_name = self.user.last_name
        super(Employee, self).save(*args, **kwargs)


class Leave(models.Model):
    NEW = 'New'
    APPROVED = 'Approved'
    DECLINED = 'Declined'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (APPROVED, 'Approved'),
        (DECLINED, 'Declined'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name='employee_pk',
    )
    days_of_leave = models.IntegerField(default=0)
    start_date = models.DateField(default=None, null=True)
    end_date = models.DateField(default=None, null=True)
    status = models.CharField(
        max_length=100,
        default=NEW,
        choices=STATUS_CHOICES
    )
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
