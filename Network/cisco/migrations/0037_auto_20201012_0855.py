# Generated by Django 3.0.8 on 2020-10-12 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cisco', '0036_auto_20201012_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_ip',
            name='EnableMonitor',
            field=models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], default='enable', max_length=100),
        ),
    ]
