# Generated by Django 2.1.5 on 2019-01-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dme', '0008_auto_20190111_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dme_ii',
            name='additional_insurance_cards',
            field=models.ImageField(blank=True, null=True, upload_to='additional_card_photo/'),
        ),
        migrations.AlterField(
            model_name='dme_ii',
            name='consent_recording',
            field=models.FileField(blank=True, null=True, upload_to='consent_recording/'),
        ),
        migrations.AlterField(
            model_name='dme_ii',
            name='insurance_card_photo_back',
            field=models.ImageField(blank=True, null=True, upload_to='card_photo', verbose_name='Insurance Card Photo(Back)'),
        ),
        migrations.AlterField(
            model_name='dme_ii',
            name='insurance_card_photo_front',
            field=models.ImageField(blank=True, null=True, upload_to='card_photo', verbose_name='Insurance Card Photo(Front)'),
        ),
        migrations.AlterField(
            model_name='dme_ii',
            name='patient_id_photo',
            field=models.ImageField(upload_to='photo_id/', verbose_name='Patient ID Photo'),
        ),
    ]