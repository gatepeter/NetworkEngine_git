# Generated by Django 3.0.8 on 2020-10-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cisco', '0034_auto_20201011_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_ip',
            name='maker',
            field=models.CharField(choices=[('Cisco', 'Cisco'), ('Juniper', 'Juniper'), ('Tp-link', 'Tp-link'), ('Huawei', 'Huawei'), ('Hkvision', 'Hkvision'), ('HP', 'HP'), ('Fortinet', 'Fortinet'), ('Other', 'Other'), ('Ubuntu', 'Ubuntu'), ('Centos', 'Centos'), ('Kali', 'Kali')], default='other', max_length=200),
        ),
    ]
