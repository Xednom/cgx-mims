# Generated by Django 2.1.4 on 2018-12-18 11:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dme', '0002_auto_20181217_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dme',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Created date of these informations'),
        ),
        migrations.AlterField(
            model_name='dme',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='dme',
            name='date_returned_for_refiling_with_remn',
            field=models.DateField(blank=True, null=True, verbose_name=django.utils.timezone.now),
        ),
    ]
