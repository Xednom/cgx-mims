# Generated by Django 2.1.4 on 2019-02-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0010_auto_20190201_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='consent_recording',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to='carrier/consent-recording/'),
        ),
    ]
