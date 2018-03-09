from django.contrib import admin

from . import models


admin.site.register(models.Catagory)
admin.site.register(models.SubCatagory)
admin.site.register(models.Product)
admin.site.register(models.MobilePhone)
admin.site.register(models.ComputerTablet)
