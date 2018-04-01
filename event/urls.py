from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^event/$', views.event_list, name='event_list'),
    url(r'^user_event/$', views.user_event_list, name='user_event_list'),
    url(r'^public_event/$', views.event_list_public, name='event_list_public'),
    url(r'^orgs/$', views.org_list, name='org_list'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.event_delete, name='event_delete'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>\d+)/addhours/$', views.event_Emp_Record, name='event_addhours'),
    url(r'^event/create/$', views.event_new, name='event_new'),
    url(r'^org/(?P<pk>\d+)/delete/$', views.org_delete, name='org_delete'),
    url(r'^orgs/(?P<pk>\d+)/edit/$', views.org_edit, name='org_edit'),
    url(r'^orgs/create/$', views.org_new, name='org_new'),


]