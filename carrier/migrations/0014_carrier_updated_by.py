# Generated by Django 2.1.4 on 2019-02-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0013_auto_20190218_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='updated_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
