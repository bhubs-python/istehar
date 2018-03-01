from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^registration-options/$', views.RegistrationOptions.as_view(), name='registration-options'),
    url(r'^registration/$', views.Registration.as_view(), name='registration'),
    url(r'^login/$', views.Login.as_view(), name='login'),

    #dashboard
    url(r'^my/dashboard/$', views.Dashboard.as_view(), name='dashboard'),

    #membership
    url(r'^my/membership/$', views.Membership.as_view(), name='membership'),

    #resume
    url(r'^my/resume/$', views.Resume.as_view(), name='resume'),
    url(r'^my/resume/add/personal/$', views.AddPersonal.as_view(), name='add-personal'),
    url(r'^my/resume/add/education/$', views.AddEducation.as_view(), name='add-education'),

    url(r'^logout/$', views.logout_request, name='logout'),
]
