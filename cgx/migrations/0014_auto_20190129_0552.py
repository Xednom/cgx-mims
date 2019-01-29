# Generated by Django 2.1.5 on 2019-01-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgx', '0013_remove_bioconfirmmaster_for_bioconfirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bioconfirmmaster',
            name='type_of_test',
            field=models.CharField(blank=True, choices=[('CARRIER', 'CARRIER'), ('CGX', 'CGX'), ('CGX/CARRIER', 'CGX/CARRIER'), ('L', 'L')], max_length=50, null=True, verbose_name='Test choices'),
        ),
    ]
