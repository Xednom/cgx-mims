# Generated by Django 2.1.4 on 2019-04-02 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgx', '0002_auto_20190306_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bioconfirmmaster',
            name='date_created',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
