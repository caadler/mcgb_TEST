from django.contrib import admin
from .models import User, Emp_Record, Event, OrgContactPerson, Organization


class UserList(admin.ModelAdmin):
    list_display = ('User_ID', 'User_Fname', 'User_Lname', 'User_Username', 'User_Email', 'User_IsActive')
    list_filter = ('User_ID', 'User_Lname', 'User_IsActive')
    ordering = ['User_ID']


class Emp_RecordList(admin.ModelAdmin):
    list_display = ('User_ID', 'EmpRecord_Validation', 'Event_ID', 'EmpRecord_Time', 'Org_ID')
    list_filter = ('User_ID', 'Event_ID', 'Org_ID')
    ordering = ['User_ID']


class EventList(admin.ModelAdmin):
    list_display = ('Event_ID', 'Org_ID', 'Event_Description', 'Event_StartTime', 'Event_EndTime',
                    'Event_StartDate', 'Event_EndDate', 'Event_Requirement', 'Event_MaxPax', 'Event_Street',
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


admin.site.register(User, UserList)
admin.site.register(Emp_Record, Emp_RecordList)
admin.site.register(Event, EventList)
admin.site.register(Organization, OrganizationList)
admin.site.register(OrgContactPerson, OrgContactPersonList)
