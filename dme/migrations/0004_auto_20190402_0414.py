# Generated by Django 2.1.4 on 2019-04-02 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dme', '0003_auto_20190402_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dme_ii',
            name='date_created',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
