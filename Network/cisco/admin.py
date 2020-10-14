from django.contrib import admin
from .models import Device_IP, ImageModel

# Register your models here.
class Device_IPadmin(admin.ModelAdmin):
    list_display = ['name','ip','description','manager','date','status']


class Image_admin(admin.ModelAdmin):
    list_display = ['myname','imageMe']


# class Person_admin(admin.ModelAdmin):
#     list_display = ['name','email','birth_date','location']




admin.site.register(Device_IP,Device_IPadmin)
admin.site.register(ImageModel,Image_admin)
# admin.site.register(Person,Person_admin)


