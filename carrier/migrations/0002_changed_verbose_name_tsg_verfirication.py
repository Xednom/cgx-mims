# Generated by Django 2.1.4 on 2019-03-07 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='insurance_verified_tsg_verification',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Insurance Verified/TSG Verification'),
        ),
    ]
