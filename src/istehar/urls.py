from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^', include('home.urls', namespace='home')),

    url(r'^staff/', include('staff.urls', namespace='staff')),
]
