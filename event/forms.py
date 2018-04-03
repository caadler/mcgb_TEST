from django import forms
from .models import Event, Organization, Emp_Record
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('Event_ID', 'Org_ID', 'Event_Description', 'Event_StartDate', 'Event_StartTime', 'Event_EndDate',
                  'Event_EndTime',
                  'Event_Requirement', 'Event_MaxPax', 'Event_Street', 'Event_City', 'Event_State',
                  'Event_Postal')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['Event_StartDate'].widget = widgets.AdminDateWidget()
        self.fields['Event_EndDate'].widget = widgets.AdminDateWidget()


class OrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ('Org_ID', 'Org_Name', 'Org_Phone', 'Org_Description', 'Org_Email', 'Org_Street',
                  'Org_City', 'Org_State', 'Org_Postal')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)



class Emp_RecordForm(forms.ModelForm):
    class Meta:
        model = Emp_Record
        fields = ('username', 'Event_ID', 'EmpRecord_Time')

class Staff_RecordForm(forms.ModelForm):
    class Meta:
        model = Emp_Record
        fields = ('Event_ID', 'EmpRecord_Time')