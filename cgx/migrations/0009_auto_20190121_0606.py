# Generated by Django 2.1.4 on 2019-01-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgx', '0008_auto_20190121_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bioconfirmmaster',
            name='status',
            field=models.CharField(blank=True, choices=[('CGX/CGD', 'CGX/CGD'), ('DUPLICATE', 'DUPLICATE'), ('HOLD', 'HOLD'), ('MISSING INFORMATION', 'MISSING INFORMATION'), ('REJECTED', 'REJECTED'), ('WRONG APPLICATION', 'WRONG APPLICATION'), ('Requires Authorization', 'Requires Authorization'), ('Resubmit from Elite', 'Resubmit from Elite'), ('RESIGNED', 'RESIGNED'), ('REJECTED HMO', 'REJECTED HMO'), ('REJECTED NO ID', 'REJECTED NO ID'), ('REJECTED INELIGIBLE', 'REJECTED INELIGIBLE'), ('REJECTED INACTIVE', 'REJECTED INACTIVE'), ('REJECTED - Higd ded 6880.37', 'REJECTED - Higd ded 6880.37'), ('REJECTED CARESOURCE', 'REJECTED CARESOURCE')], max_length=50, null=True, verbose_name='Status'),
        ),
    ]