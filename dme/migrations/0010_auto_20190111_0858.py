# Generated by Django 2.1.5 on 2019-01-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dme', '0009_auto_20190111_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dme_ii',
            name='consent_recording',
            field=models.ImageField(blank=True, null=True, upload_to='consent_recording/'),
        ),
    ]