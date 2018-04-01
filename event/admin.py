from django.contrib import admin
from django.contrib.auth.models import User
from .models import Emp_Record, Event, OrgContactPerson, Organization



class Emp_RecordList(admin.ModelAdmin):
    list_display = ('username', 'Event_ID', 'EmpRecord_Time')
    list_filter = ('username', 'Event_ID')
    ordering = ['username']


class EventList(admin.ModelAdmin):
    list_display = ('Event_ID', 'Org_ID', 'Event_Description', 'Event_StartDate', 'Event_StartTime',
                     'Event_EndDate', 'Event_EndTime', 'Event_Requirement', 'Event_MaxPax', 'Event_Street',
                    'Event_City', 'Event_State', 'Event_Postal')
    list_filter = ('Event_ID', 'Org_ID', 'Event_StartDate', 'Event_City')
    ordering = ['Event_ID']


class OrganizationList(admin.ModelAdmin):
    list_display = ('Org_ID', 'Org_Name', 'Org_Phone', 'Org_Description')
    list_filter = ('Org_ID', 'Org_Name')
    ordering = ['Org_ID']


class OrgContactPersonList(admin.ModelAdmin):
    list_display = ('Org_Contact_Fname', 'Org_Contact_Lname', 'Org_Contact_Position')
    ordering = ['Org_Contact_Lname']







admin.site.register(Emp_Record, Emp_RecordList)
admin.site.register(Event, EventList)
admin.site.register(Organization, OrganizationList)
admin.site.register(OrgContactPerson, OrgContactPersonList)
