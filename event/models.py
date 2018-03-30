from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

STATES = [
    ('Alabama', 'AL'),
    ('Alaska', 'AK'),
    ('Arizona', 'AZ'),
    ('Arkansas', 'AR'),
    ('California', 'CA'),
    ('Colorado', 'CO'),
    ('Connecticut', 'CT'),
    ('Delaware', 'DE'),
    ('Florida', 'FL'),
    ('Georgia', 'GA'),
    ('Hawaii', 'HI'),
    ('Idaho', 'ID'),
    ('Illinois', 'IL'),
    ('Indiana', 'IN'),
    ('Iowa', 'IA'),
    ('Kansas', 'KS'),
    ('Kentucky', 'KY'),
    ('Louisiana', 'LA'),
    ('Maine', 'ME'),
    ('Maryland', 'MD'),
    ('Massachusetts', 'MA'),
    ('Michigan', 'MI'),
    ('Minnesota', 'MN'),
    ('Mississippi', 'MS'),
    ('Missouri', 'MO'),
    ('Montana', 'MT'),
    ('Nebraska', 'NE'),
    ('Nevada', 'NV'),
    ('New Hampshire', 'NH'),
    ('New Jersey', 'NJ'),
    ('New Mexico', 'NM'),
    ('New York', 'NY'),
    ('North Carolina', 'NC'),
    ('North Dakota', 'ND'),
    ('Ohio', 'OH'),
    ('Oklahoma', 'OK'),
    ('Oregon', 'OR'),
    ('Pennsylvania', 'PA'),
    ('Rhode Island', 'RI'),
    ('South Carolina', 'SC'),
    ('South Dakota', 'SD'),
    ('Tennessee', 'TN'),
    ('Texas', 'TX'),
    ('Utah', 'UT'),
    ('Vermont', 'VT'),
    ('Virginia', 'VA'),
    ('Washington', 'WA'),
    ('West Virginia', 'WV'),
    ('Wisconsin', 'WI'),
    ('Wyoming', 'WY'),
    ]

TIMES = [
    ('00:00AM', '00:00'),
    ('00:30AM', '00:30'),
    ('01:00AM', '01:00'),
    ('01:30AM', '01:30'),
    ('02:00AM', '02:00'),
    ('02:30AM', '02:30'),
    ('03:00AM', '03:00'),
    ('03:30AM', '03:30'),
    ('04:00AM', '04:00'),
    ('04:30AM', '04:30'),
    ('05:00AM', '05:00'),
    ('05:30AM', '05:30'),
    ('06:00AM', '06:00'),
    ('06:30AM', '06:30'),
    ('07:00AM', '07:00'),
    ('07:30AM', '07:30'),
    ('08:00AM', '08:00'),
    ('08:30AM', '08:30'),
    ('09:00AM', '09:00'),
    ('09:30AM', '09:30'),
    ('10:00AM', '10:00'),
    ('10:30AM', '10:30'),
    ('11:00AM', '11:00'),
    ('11:30AM', '11:30'),
    ('12:00PM', '12:00'),
    ('00:30PM', '12:30'),
    ('01:00PM', '13:00'),
    ('01:30PM', '13:30'),
    ('02:00PM', '14:00'),
    ('02:30PM', '14:30'),
    ('03:00PM', '15:00'),
    ('03:30PM', '15:30'),
    ('04:00PM', '16:00'),
    ('04:30PM', '16:30'),
    ('05:00PM', '17:00'),
    ('05:30PM', '17:30'),
    ('06:00PM', '18:00'),
    ('06:30PM', '18:30'),
    ('07:00PM', '19:00'),
    ('07:30PM', '19:30'),
    ('08:00PM', '20:00'),
    ('08:30PM', '20:30'),
    ('09:00PM', '21:00'),
    ('09:30PM', '21:30'),
    ('10:00PM', '22:00'),
    ('10:30PM', '22:30'),
    ('11:00PM', '23:00'),
    ('11:30PM', '23:30'),
    ]
class User(models.Model):
    User_ID = models.IntegerField(blank=False, null=False)
    User_Password = models.CharField(max_length=50)
    User_Fname = models.CharField(max_length=50)
    User_Lname = models.CharField(max_length=50)
    User_Username = models.CharField(max_length=50)
    User_Lastlogin = models.DateTimeField(default=timezone.now)
    User_Datejoined = models.DateField(default=timezone.now)
    User_Email = models.CharField(max_length=50)
    User_IsActive = models.CharField(max_length=50)
    User_IsSuperuser = models.CharField(max_length=50)

    def created(self):
        self.User_Datejoined = timezone.now()
        self.save()

    def updated(self):
        self.save()

    def __str__(self):
        return str(self.User_ID)


class Group(models.Model):
    Group_ID = models.IntegerField(blank=False, null=False)
    Group_Name = models.CharField(max_length=50)
    User_ID = models.ForeignKey(User, related_name='groups')

    def created(self):
        self.save()

    def __str__(self):
        return str(self.Group_ID)


class User_Permission(models.Model):
    User_Permission_ID = models.IntegerField(blank=False, null=False)
    Auth_Permission_ID = models.IntegerField(blank=False, null=False)
    User_ID = models.ForeignKey(User, related_name='user_permissions')

    def created(self):
        self.save()

    def __str__(self):
        return str(self.User_ID)


class Organization(models.Model):
    Org_ID = models.IntegerField(blank=False, null=False, unique=True)
    Org_Name = models.CharField(max_length=50)
    Org_Phone = models.IntegerField(blank=False, null=False, max_length=9)
    Org_Description = models.CharField(max_length=500)
    Org_Email = models.CharField(max_length=50)
    Org_Street = models.CharField(max_length=50)
    Org_City = models.CharField(max_length=50)
    Org_State = models.CharField(max_length=20, choices=STATES)
    Org_Postal = models.IntegerField(blank=False, null=False)

    def created(self):
        self.save()

    def __str__(self):
        return str(self.Org_ID)


class OrgContactPerson(models.Model):
    Org_ID = models.ForeignKey(Organization, related_name='orgContactPersons')
    Org_Contact_Fname = models.CharField(max_length=50)
    Org_Contact_Lname = models.CharField(max_length=50)
    Org_Contact_Phone = models.CharField(max_length=9)
    Org_contact_Email = models.CharField(max_length=50)
    Org_Contact_Position = models.CharField(max_length=50)

    def created(self):
        self.save()


class Event(models.Model):

    Event_ID = models.IntegerField(blank=False, null=False, unique=True)
    Org_ID = models.ForeignKey(Organization, related_name='events')
    Event_Description = models.CharField(max_length=500)
    Event_StartTime = models.CharField(max_length=10, choices=TIMES)
    Event_EndTime = models.CharField(max_length=10, choices=TIMES)
    Event_StartDate = models.DateField(default=timezone.now)
    Event_EndDate = models.DateField(default=timezone.now)
    Event_Requirement = models.CharField(max_length=50)
    Event_MaxPax = models.IntegerField(blank=False)
    Event_Street = models.CharField(max_length=50)
    Event_City = models.CharField(max_length=50)
    Event_State = models.CharField(max_length=20, choices=STATES)
    Event_Postal = models.IntegerField(blank=False, null=False)
    Event_Hour = models.IntegerField(default=0)

    def created(self):
        self.save()


class Emp_Record(models.Model):
    User_ID = models.ForeignKey(User)
    EmpRecord_Validation = models.BooleanField
    Event_ID = models.ForeignKey(Event)
    EmpRecord_Time = models.DecimalField(max_digits=3, decimal_places=2)
    Org_ID = models.ForeignKey(Organization)

    def created(self):
        self.save()


class AddHour(models.Model):
    EmpRecord_Time = models.DecimalField(max_digits=2, decimal_places=2)

    def created(self):
        self.save()
