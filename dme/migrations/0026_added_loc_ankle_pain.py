# Generated by Django 2.1.4 on 2019-02-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dme', '0025_auto_20190221_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='dme_ii',
            name='location_of_ankle_pain',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
