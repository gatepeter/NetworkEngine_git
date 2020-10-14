from import_export import resources
from .models import  Device_IP

# class PersonResource(resources.ModelResource):
#     class Meta:
#         model = Person


class DeviceIPResource(resources.ModelResource):
    class Meta:
        model = Device_IP