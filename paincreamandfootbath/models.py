import uuid
import datetime
from django.db import models

from cgx.models import Agent


class PainCreamAndFootBath(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    submission_date = models.DateField(default=datetime.date.today)
    promo_code = models.CharField(max_length=100, null=True, blank=True)
    agent_name = models.ForeignKey(Agent, verbose_name="Agent name", on_delete=models.PROTECT, null=True, blank=True)
    agent_email = models.EmailField(max_length=100, null=True, blank=True)
    patient_first_name = models.CharField(max_length=250, default="n/a", verbose_name="Patient's First Name", null=True, blank=True)
    patient_last_name = models.CharField(max_length=250, default="n/a", verbose_name="Patient's Last Name", null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    patient_phone_number = models.CharField(max_length=100, default="n/a", null=True, blank=True)
    best_time_to_call = models.CharField(max_length=100, default="n/a", null=True, blank=True)
    street_address = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    street_address_2 = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    city = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    state_province = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    postal_zip_code = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    country = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    insurance_type = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    medicare_medicaid_policy = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    ppo_hmo_information_mem_id = models.CharField(max_length=250, default="n/a", verbose_name='PPO/HMO Information (If not straight Medicare)(Medicare ID#)')
    ppo_hmo_information_ppo_name = models.CharField(max_length=250, default="n/a", verbose_name='PPO/HMO Information(If not straight Medicare)(PPO Name)', null=True, blank=True)
    insurance_status = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    location_of_pain = models.CharField(max_length=250, default="n/a", null=True, blank=True)
    level_of_pain = models.CharField(max_length=100, default="n/a", null=True, blank=True)
    discomfort = models.CharField(max_length=250, default='n/a', verbose_name='How long have you been experiencing discomfort?', null=True, blank=True)
    feq_of_pain = models.CharField(max_length=100, default='n/a', verbose_name='Frequency of pain', null=True, blank=True)
    prescribe_pain_cream = models.CharField(max_length=250, default='n/a',
                                               verbose_name='Based upon the level of pain to the areas the patient is requesting braces and/or foot pain. would the patient also like for the doctor to prescribe pain cream?',
                                               null=True, blank=True)
    location_of_foot_issue = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    describe_foot_issue = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    order_status = models.CharField(max_length=150, default='n/a', null=True, blank=True)
    date_faxed_to_pharmacy = models.DateField(null=True, blank=True)
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, verbose_name='IP Address', null=True, blank=True)
    submission_id = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    patient_id_photo = models.ImageField(upload_to='pc_fb/patient-id-photo/', max_length=1000, null=True, blank=True)
    insurance_card_photo = models.ImageField(upload_to='pc_fb/insurance-card-photo/', max_length=1000, null=True, blank=True)
    ppo_card_photo = models.ImageField(upload_to='pc_fb/ppo-card-photo/', max_length=1000, null=True, blank=True)
    consent_recording = models.FileField(upload_to='pc_fb/consent-recording/', max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.datetime.today, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    user_promo_code = models.CharField(max_length=100, verbose_name="Promo code of the agent who created this record.", null=True, blank=True)

    class Meta:
        verbose_name = 'Pain Cream and Foot Bath'
        verbose_name_plural = 'Pain Cream and Foot Baths'
        ordering = ['submission_date']

    def __str__(self):
        return str(self.submission_date)
