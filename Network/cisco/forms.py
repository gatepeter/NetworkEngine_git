from django import forms
from .models import Device_IP, ImageModel


class DeviceIPForm(forms.ModelForm):
    class Meta:
        model = Device_IP
        fields = ('name', 'ip', 'DeviceType','description', 'maker','manager','EnableMonitor','status',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ('imageMe',)


