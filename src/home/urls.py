from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),

    #post ad url
    url(r'^post-ad/$', views.PostAd.as_view(), name='post-ad'),
    url(r'^post-ad/category/$', views.PostCategory.as_view(), name='post-category'),
    url(r'^post-ad/location/$', views.PostLocation.as_view(), name='post-location'),

    url(r'^post-ad/details/$', views.PostDetails.as_view(), name='post-details'),
]
