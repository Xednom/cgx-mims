# Generated by Django 2.1.4 on 2019-03-05 06:49

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cgx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PainCreamAndFootBath',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('submission_date', models.DateField(default=datetime.date.today)),
                ('promo_code', models.CharField(blank=True, max_length=100, null=True)),
                ('agent_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('patient_first_name', models.CharField(blank=True, default='n/a', max_length=250, null=True, verbose_name="Patient's First Name")),
                ('patient_last_name', models.CharField(blank=True, default='n/a', max_length=250, null=True, verbose_name="Patient's Last Name")),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=100, null=True)),
                ('patient_phone_number', models.CharField(blank=True, default='n/a', max_length=100, null=True)),
                ('best_time_to_call', models.CharField(blank=True, default='n/a', max_length=100, null=True)),
                ('street_address', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('street_address_2', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('city', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('state_province', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('postal_zip_code', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('country', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('insurance_type', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('medicare_medicaid_policy', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('ppo_hmo_information_mem_id', models.CharField(default='n/a', max_length=250, verbose_name='PPO/HMO Information (If not straight Medicare)(Medicare ID#)')),
                ('ppo_hmo_information_ppo_name', models.CharField(blank=True, default='n/a', max_length=250, null=True, verbose_name='PPO/HMO Information(If not straight Medicare)(PPO Name)')),
                ('insurance_status', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('location_of_pain', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('level_of_pain', models.CharField(blank=True, default='n/a', max_length=100, null=True)),
                ('discomfort', models.CharField(blank=True, default='n/a', max_length=250, null=True, verbose_name='How long have you been experiencing discomfort?')),
                ('feq_of_pain', models.CharField(blank=True, default='n/a', max_length=100, null=True, verbose_name='Frequency of pain')),
                ('prescribe_pain_cream', models.CharField(blank=True, default='n/a', max_length=250, null=True, verbose_name='Based upon the level of pain to the areas the patient is requesting braces and/or foot pain. would the patient also like for the doctor to prescribe pain cream?')),
                ('location_of_foot_issue', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('describe_foot_issue', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('order_status', models.CharField(blank=True, default='n/a', max_length=150, null=True)),
                ('date_faxed_to_pharmacy', models.DateField(blank=True, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP Address')),
                ('submission_id', models.CharField(blank=True, default='n/a', max_length=250, null=True)),
                ('patient_id_photo', models.ImageField(blank=True, max_length=1000, null=True, upload_to='pc_fb/patient-id-photo/')),
                ('insurance_card_photo', models.ImageField(blank=True, max_length=1000, null=True, upload_to='pc_fb/insurance-card-photo/')),
                ('ppo_card_photo', models.ImageField(blank=True, max_length=1000, null=True, upload_to='pc_fb/ppo-card-photo/')),
                ('consent_recording', models.FileField(blank=True, max_length=1000, null=True, upload_to='pc_fb/consent-recording/')),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.today, null=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user_promo_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Promo code of the agent who created this record.')),
                ('agent_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cgx.Agent', verbose_name='Agent name')),
            ],
            options={
                'verbose_name': 'Pain Cream and Foot Bath',
                'verbose_name_plural': 'Pain Cream and Foot Baths',
                'ordering': ['submission_date'],
            },
        ),
    ]
