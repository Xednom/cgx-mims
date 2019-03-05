# Generated by Django 2.1.4 on 2019-03-05 04:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cgx', '0027_updates_on_dates_and_test_status_choices'),
        ('carrier', '0017_auto_20190224_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrier',
            name='submitted_to_tamika_ins_verifier',
        ),
        migrations.AddField(
            model_name='carrier',
            name='insurance_verified_tsg_verification',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='INSURANCE VERIFIED/TSG VERIFICATION'),
        ),
        migrations.AddField(
            model_name='carrier',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cgx.Manager', verbose_name='Manager name'),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='status',
            field=models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.PROTECT, to='cgx.Status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='type_of_test',
            field=models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.PROTECT, to='cgx.Test_choices', verbose_name='Test choices'),
        ),
    ]
