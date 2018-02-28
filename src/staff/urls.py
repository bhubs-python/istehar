from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),

    #add division
    url(r'^add-division/$', views.AddDivision.as_view(), name='add-division'),

    #add district
    url(r'^add-district/division/$', views.AddDistrictDivisionList.as_view(), name='add-district-division-list'),
    url(r'^add-district/division/(?P<division>[a-zA-Z0-9-_]+)/$', views.AddDistrict.as_view(), name='add-district'),

    #add thana
    url(r'^add-thana/division/$', views.AddThanaDivisionList.as_view(), name='add-thana-division-list'),
    url(r'^add-thana/(?P<division>[a-zA-Z0-9-_]+)/$', views.AddThanaDistrictList.as_view(), name='add-thana-district-list'),
    url(r'^add-thana/(?P<division>[a-zA-Z0-9-_]+)/(?P<district>[0-9]+)/$', views.AddThana.as_view(), name='add-thana'),
]
