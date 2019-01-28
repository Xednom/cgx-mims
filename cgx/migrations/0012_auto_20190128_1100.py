# Generated by Django 2.1.5 on 2019-01-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgx', '0011_bioconfirmmaster_for_bioconfirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Agent name'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Manager name'),
        ),
    ]
