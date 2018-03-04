from django.contrib import admin

from . import models


admin.site.register(models.Personal)
admin.site.register(models.Education)
admin.site.register(models.Professional)
admin.site.register(models.PastEmployment)
admin.site.register(models.PermanentLocation)

