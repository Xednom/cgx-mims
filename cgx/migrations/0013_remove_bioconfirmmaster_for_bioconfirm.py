# Generated by Django 2.1.5 on 2019-01-28 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cgx', '0012_auto_20190128_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bioconfirmmaster',
            name='for_bioconfirm',
        ),
    ]