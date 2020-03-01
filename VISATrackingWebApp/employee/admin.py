from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employee, MasterProcess, VisaApplication, VisaApplicationProcess, Team


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Employee Details", {"fields": ["first_name", "last_name", "email_id", "manager_id", "team_id"]}),
    ]


class MasterProcessAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Master Process", {"fields": ["process_title", "process_description", "next_process"]})
    ]


class VisaApplicationAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Visa Application", {"fields": ["employee_id", "manager", "people_partner_id"]})
    ]


class VisaApplicationProcessAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Visa Application Process",
         {"fields": ["master_process_id", "visa_application_id", "description_log", "created_by", "pending_on"]})
    ]


class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Team Details",
         {"fields": ["team_name", "customer_id"]})
    ]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(MasterProcess, MasterProcessAdmin)
admin.site.register(VisaApplication, VisaApplicationAdmin)
admin.site.register(VisaApplicationProcess, VisaApplicationProcessAdmin)
admin.site.register(Team, TeamAdmin)
