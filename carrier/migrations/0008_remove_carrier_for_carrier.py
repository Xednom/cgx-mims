# Generated by Django 2.1.5 on 2019-01-28 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0007_auto_20190128_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrier',
            name='for_carrier',
        ),
    ]
