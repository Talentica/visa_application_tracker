from django.db import models
from datetime import datetime


# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name


class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email_id = models.CharField(max_length=100, null=True, blank=True)
    manager_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name


class MasterProcess(models.Model):
    process_title = models.CharField(max_length=50)
    process_description = models.CharField(max_length=200)
    next_process = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.process_title


class VisaApplication(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_id')
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='manager', null=True, blank=True)
    people_partner_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='people_partner_id',
                                          null=True, blank=True)


class VisaApplicationProcess(models.Model):
    master_process_id = models.ForeignKey(MasterProcess, on_delete=models.CASCADE, default=1)
    visa_application_id = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    description_log = models.CharField(max_length=200)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="created_by")
    pending_on = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, related_name="pending_on")
    date_created = models.DateTimeField("date created", default=datetime.now())

