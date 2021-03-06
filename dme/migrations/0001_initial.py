# Generated by Django 2.1.4 on 2019-03-05 06:49

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DME_II',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('submission_date', models.DateField(default=datetime.date.today)),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('agents_promod_code', models.CharField(blank=True, max_length=100, null=True, verbose_name="Agent's Promo Code")),
                ('agents_email', models.EmailField(blank=True, max_length=100, null=True, verbose_name="Agent's Email")),
                ('patients_first_name', models.CharField(blank=True, max_length=250, null=True, verbose_name="Patient's First Name")),
                ('patients_last_name', models.CharField(blank=True, max_length=250, null=True, verbose_name="Patient's Last Name")),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=100, null=True)),
                ('patients_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name="Patient's Phone Number")),
                ('best_time_to_call', models.CharField(blank=True, max_length=250, null=True)),
                ('street_address', models.CharField(blank=True, max_length=250, null=True)),
                ('street_address_line_2', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('state_province', models.CharField(blank=True, max_length=250, null=True, verbose_name='State/Province')),
                ('postal_zip_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Postal/Zip Code')),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('patient_id_photo', models.ImageField(blank=True, null=True, upload_to='dme/patient-id-photo/', verbose_name='Patient ID Photo')),
                ('insurance_type', models.CharField(blank=True, max_length=250, null=True)),
                ('policy_number', models.CharField(blank=True, max_length=250, null=True, verbose_name='Policy Number(Medicare)')),
                ('ppo_information_mem_id', models.CharField(blank=True, max_length=250, null=True, verbose_name='PPO Information(If not straight from Medicare)(Member ID#)')),
                ('ppo_information_ppo_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='PPO Information(If not straight from Medicare)(PPO Name)')),
                ('insurance_status', models.CharField(blank=True, max_length=250, null=True)),
                ('insurance_notes', models.TextField(blank=True, null=True)),
                ('insurance_card_photo_front', models.ImageField(blank=True, max_length=1000, null=True, upload_to='dme/insurance-card-photo-front/', verbose_name='Insurance Card Photo(Front)')),
                ('insurance_card_photo_back', models.ImageField(blank=True, max_length=1000, null=True, upload_to='dme/insurance-card-photo-back/', verbose_name='Insurance Card Photo(Back)')),
                ('additional_insurance_cards', models.ImageField(blank=True, max_length=1000, null=True, upload_to='dme/additional-card-photo/')),
                ('location_of_back_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('location_of_shoulder_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('location_of_knee_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('location_of_ankle_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('location_of_elbow_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('location_of_wrist_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('height', models.CharField(blank=True, max_length=250, null=True)),
                ('weight', models.CharField(blank=True, max_length=250, null=True)),
                ('size_of_brace', models.CharField(blank=True, max_length=250, null=True)),
                ('major_medical_conditions', models.CharField(blank=True, max_length=250, null=True)),
                ('cause_of_pain_discomfort', models.CharField(blank=True, max_length=250, null=True, verbose_name='Cause of Pain/Discomfort')),
                ('level_of_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('experiencing_discomfort', models.CharField(blank=True, max_length=250, null=True, verbose_name='How long have you been experiencing discomfort')),
                ('frequency_of_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('describe_pain', models.CharField(blank=True, max_length=250, null=True)),
                ('pain_symptoms', models.CharField(blank=True, max_length=250, null=True)),
                ('pain_worse', models.CharField(blank=True, max_length=250, null=True, verbose_name='What makes the Pain Worse')),
                ('treatments_tried', models.CharField(blank=True, max_length=250, null=True)),
                ('seen_doctor', models.CharField(blank=True, max_length=250, null=True, verbose_name='Have you seen a doctor in the last year?')),
                ('surgeries', models.CharField(blank=True, max_length=250, null=True, verbose_name='Any Surgeries in the last year?')),
                ('consent_recording', models.ImageField(blank=True, max_length=1000, null=True, upload_to='dme/consent-recording/')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP Address')),
                ('submission_id', models.CharField(blank=True, max_length=350, null=True)),
                ('edit_link', models.CharField(blank=True, max_length=250, null=True)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.today, null=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user_promo_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Promo code of the agent who created this record.')),
            ],
            options={
                'verbose_name': 'DME II',
                'verbose_name_plural': 'DME II',
                'ordering': ['-submission_date'],
            },
        ),
    ]
