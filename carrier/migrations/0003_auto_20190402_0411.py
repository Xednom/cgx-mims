# Generated by Django 2.1.4 on 2019-04-02 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0002_changed_verbose_name_tsg_verfirication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='date_created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
