from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import *
from django.db.models import Sum


def home(request):
    return render(request, 'event/home.html',
                  {'event': home})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'event/home.html',
                  {'event': home})
    else:
        form = SignUpForm()
    return render(request, 'event/signup.html', {'form': form})




def event_list_public(request):
    events = Event.objects.filter(Event_StartDate__lte=timezone.now())
    return render(request, 'event/event_list_public.html',
                  {'events': events})



@login_required
def user_event_list(request):
    events = Event.objects.filter(Event_StartDate__lte=timezone.now())
    return render(request, 'event/user_event_list.html',
                  {'events': events})




@login_required
def event_list(request):
    events = Event.objects.filter(Event_StartDate__lte=timezone.now())
    return render(request, 'event/event_list.html',
                  {'events': events})


@login_required
def org_list(request):
    orgs = Organization.objects.filter()
    return render(request, 'event/org_list.html',
                  {'orgs': orgs})


@login_required
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_date = timezone.now()
            event.save()
            events = Event.objects.filter()
            return render(request, 'event/event_list.html',
                          {'events': events})
    else:
        form = EventForm()
    return render(request, 'event/event_new.html', {'form': form})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        # update
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            event = Event.objects.filter()
            return render(request, 'event/event_list.html', {'events': event})
    else:
        form = EventForm(instance=event)
    return render(request, 'event/event_edit.html', {'form': form})


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    events = Event.objects.filter()
    return render(request, 'event/event_list.html', {'events': events})


@login_required
def org_new(request):
    if request.method == "POST":
        form = OrgForm(request.POST)
        if form.is_valid():
            org = form.save(commit=False)
            org.created_date = timezone.now()
            org.save()
            orgs = Organization.objects.filter()
            return render(request, 'event/org_list.html',
                          {'orgs': orgs})
    else:
        form = OrgForm()
    # print("Else")
    return render(request, 'event/org_new.html', {'form': form})


@login_required
def org_edit(request, pk):
    org = get_object_or_404(Organization, pk=pk)
    if request.method == "POST":
        # update
        form = OrgForm(request.POST, instance=org)
        if form.is_valid():
            org = form.save(commit=False)
            org.save()
            org = Organization.objects.filter()
            return render(request, 'event/org_list.html', {'orgs': org})
    else:
        form = OrgForm(instance=org)
    return render(request, 'event/org_edit.html', {'form': form})


@login_required
def org_delete(request, pk):
    org = get_object_or_404(Organization, pk=pk)
    org.delete()
    orgs = Organization.objects.filter()
    return render(request, 'event/org_list.html', {'orgs': orgs})

