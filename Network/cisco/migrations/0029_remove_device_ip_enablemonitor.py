# Generated by Django 3.0.8 on 2020-09-29 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cisco', '0028_device_ip_enablemonitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device_ip',
            name='EnableMonitor',
        ),
    ]
