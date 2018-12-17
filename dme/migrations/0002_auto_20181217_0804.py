# Generated by Django 2.1.4 on 2018-12-17 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dme',
            name='created_at',
            field=models.DateField(default=datetime.date(2018, 12, 17), verbose_name='Created date of these informations'),
        ),
        migrations.AlterField(
            model_name='dme',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2018, 12, 17), null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='dme',
            name='date_returned_for_refiling_with_remn',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.date(2018, 12, 17)),
        ),
    ]
