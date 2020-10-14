from django.db import models
from django.contrib.auth.models import User
# import django
# Create your models here.

Human_REC = (
    ('admin','admin'),
    ('Linhnh', 'Linhnh'),
    ('Phonght','Phonght'),
)
# kiểu charfield luôn là string không thể là số. Error 28092020

CHOICES = [
        ('Enable','Enable'),
        ('Disable','Disable'),
]

Device_Type = [
        ('Router','Router'),
        ('Switch','Switch'),
        ('Firewall','Firewall'),
        ('Server','Server'),
        ('Modem','Modem'),
        ('Print','Print'),
        ('Camera','Camera'),
        ('Camera Record','Camera Record'),
        ('Database','Database'),
        ('Other','Other'),
]

Product = [
        ('Cisco','Cisco'),
        ('Juniper','Juniper'),
        ('Tp-link','Tp-link'),
        ('Huawei','Huawei'),
        ('Hkvision','Hkvision'),
        ('HP','HP'),
        ('Fortinet','Fortinet'),
        ('Other','Other'),
        ('Ubuntu','Ubuntu'),
        ('Centos','Centos'),
        ('Kali','Kali'),
        ('Window','Window'),
]

class Device_IP(models.Model):
    name = models.CharField(max_length=100, default='', null= False, blank=False)
    ip = models.CharField(max_length=50, default='', null =  False, blank=False)
    status = models.BooleanField(default=True)
    DeviceType = models.CharField(max_length=200, default='Other', choices=Device_Type)
    description = models.CharField(max_length=200, default='')
    maker = models.CharField(max_length=200, default='Other', choices=Product)
    manager = models.CharField(max_length=50, choices=Human_REC, default='Linhnh')
    EnableMonitor = models.CharField(max_length=100, choices=CHOICES, default='Enable')
    # manager = models.CharField(max_length=50, choices=Human_REC, default='Linhnh')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Server(models.Model):
    hostname =models.CharField(max_length=100, default='')
    ip =models.CharField(max_length=100, default='')
    cpu =models.CharField(max_length=100, default='')
    ram =models.CharField(max_length=100, default='')
    hardisk =models.CharField(max_length=100, default='')


class ImageModel(models.Model):
    myname = models.CharField(max_length=20, default='')
    imageMe = models.ImageField(null=True)

    def __str__(self):
        return self.myname


# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(blank=True)
#     birth_date = models.DateField()
#     location = models.CharField(max_length=100, blank=True)