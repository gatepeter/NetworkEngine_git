# Generated by Django 3.1 on 2020-08-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cisco', '0002_device_ip_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_ip',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
