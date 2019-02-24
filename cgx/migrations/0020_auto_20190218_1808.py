# Generated by Django 2.1.4 on 2019-02-18 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgx', '0019_auto_20190210_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='bioconfirmmaster',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bioconfirmmaster',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today, null=True),
        ),
        migrations.AddField(
            model_name='bioconfirmmaster',
            name='user_promo_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
