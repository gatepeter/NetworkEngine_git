# Generated by Django 3.1 on 2020-08-26 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cisco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device_ip',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
