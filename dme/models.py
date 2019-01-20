import uuid
import datetime
from django.db import models

from django.utils import timezone
from django.utils.safestring import mark_safe

from cgx.models import Manager


PPO_S_PLUS_S_CHECKING = 1
SENT_TO_CGS_CHECK = 2
SENT_TO_PPO_CHECK = 3
SENT_TO_DME = 4
SENT_TO_TELEMED = 5


PATIENT_STATUS_CHOICES = (
    (PPO_S_PLUS_S_CHECKING, 'PPO S+S Checking'),
    (SENT_TO_CGS_CHECK, 'Sent to CGS Check'),
    (SENT_TO_PPO_CHECK, 'Sent to PPO Check'),
    (SENT_TO_DME, 'Sent to DME'),
    (SENT_TO_TELEMED, 'Sent to Telemed')
)

GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)


class DME(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent_id = models.CharField(max_length=250, verbose_name='Agent ID Number')
    manager_name = models.ForeignKey(Manager, verbose_name='Manager Name', on_delete=models.PROTECT, null=True, blank=True)
    patient_id = models.CharField(max_length=250, verbose_name='Patient ID Number', null=True, blank=True)
    date = models.DateField(default=timezone.now, verbose_name='Date', null=True, blank=True)
    sent_to_telemed = models.CharField(max_length=250, verbose_name='Sent to Telemed', null=True, blank=True)
    patient_status = models.CharField(max_length=2, choices=PATIENT_STATUS_CHOICES, null=True, blank=True)
    date_returned_for_refiling_with_remn = models.DateField(default=timezone.now, null=True, blank=True, verbose_name='Date returned for refiling with Remn')
    eligibility_verified = models.CharField(max_length=250, verbose_name='Eligibility Verified', null=True, blank=True)
    patient_first_name = models.CharField(max_length=250, verbose_name="Patient's First Name", null=True, blank=True)
    patient_last_name = models.CharField(max_length=250, verbose_name="Patient's Last Name", null=True, blank=True)
    primary_insurance_name = models.CharField(max_length=250, verbose_name='Primary Insurance Name', null=True, blank=True)
    braces_requested = models.CharField(max_length=250, verbose_name='Braces Requested', null=True, blank=True)
    braces_s_plus_s_approved = models.CharField(max_length=250, verbose_name='Braces S+S approved', null=True, blank=True)
    braces_shipped = models.CharField(max_length=250, verbose_name='Braces Shipped', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateField(default=timezone.now, verbose_name='Created date of these informations')
    updated_at = models.DateField(verbose_name='Date updated')
    who_updated = models.CharField(max_length=150, verbose_name='User who updated these informations')

    class Meta:
        verbose_name = 'DME'
        verbose_name_plural = 'DME'
        ordering = ['-date']

    def __str__(self):
        return self.patient_first_name + self.patient_last_name


class DME_II(models.Model):
    submission_date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    agents_promod_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="Agent's Promo Code")
    agents_email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="Agent's Email")
    patients_first_name = models.CharField(max_length=250, null=True, blank=True, verbose_name="Patient's First Name")
    patients_last_name = models.CharField(max_length=250, null=True, blank=True, verbose_name="Patient's Last Name")
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    patients_phone_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Patient's Phone Number")
    best_time_to_call = models.CharField(max_length=250, null=True, blank=True)
    street_address = models.CharField(max_length=250, null=True, blank=True)
    street_address_line_2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    state_province = models.CharField(max_length=250, null=True, blank=True, verbose_name='State/Province')
    postal_zip_code = models.CharField(max_length=100, null=True, blank=True, verbose_name='Postal/Zip Code')
    country = models.CharField(max_length=250, null=True, blank=True,)
    patient_id_photo = models.ImageField(upload_to='photo_id/', max_length=100, verbose_name='Patient ID Photo')
    insurance_type = models.CharField(max_length=250, null=True, blank=True)
    policy_number = models.CharField(max_length=250, null=True, blank=True, verbose_name='Policy Number(Medicare)')
    ppo_information_mem_id = models.CharField(max_length=250, null=True, blank=True, verbose_name='PPO Information(If not straight from Medicare)(Member ID#)')
    ppo_information_ppo_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='PPO Information(If not straight from Medicare)(PPO Name)')
    insurance_status = models.CharField(max_length=250, null=True, blank=True)
    insurance_notes = models.TextField(null=True, blank=True)
    insurance_card_photo_front = models.ImageField(upload_to='card_photo', max_length=100, null=True, blank=True, verbose_name='Insurance Card Photo(Front)')
    insurance_card_photo_back = models.ImageField(upload_to='card_photo',max_length=100, null=True, blank=True, verbose_name='Insurance Card Photo(Back)')
    additional_insurance_cards = models.ImageField(upload_to='additional_card_photo/',max_length=100, null=True, blank=True)
    location_of_back_pain = models.CharField(max_length=250, null=True, blank=True)
    location_of_shoulder_pain = models.CharField(max_length=250, null=True, blank=True)
    location_of_knee_pain = models.CharField(max_length=250, null=True, blank=True)
    location_of_elbow_pain = models.CharField(max_length=250, null=True, blank=True)
    localtion_of_wrist_pain = models.CharField(max_length=250, null=True, blank=True)
    height = models.CharField(max_length=250, null=True, blank=True)
    weight = models.CharField(max_length=250, null=True, blank=True)
    size_of_brace = models.CharField(max_length=250, null=True, blank=True)
    major_medical_conditions = models.CharField(max_length=250, null=True, blank=True)
    cause_of_pain_discomfort = models.CharField(max_length=250, null=True, blank=True, verbose_name='Cause of Pain/Discomfort')
    level_of_pain = models.CharField(max_length=250, null=True, blank=True)
    experiencing_discomfort = models.CharField(max_length=250, null=True, blank=True, verbose_name='How long have you been experiencing discomfort')
    frequency_of_pain = models.CharField(max_length=250, null=True, blank=True)
    describe_pain = models.CharField(max_length=250, null=True, blank=True)
    pain_symptoms = models.CharField(max_length=250, null=True, blank=True)
    pain_worse = models.CharField(max_length=250, null=True, blank=True, verbose_name='What makes the Pain Worse')
    treatments_tried = models.CharField(max_length=250, null=True, blank=True)
    seen_doctor = models.CharField(max_length=250, null=True, blank=True, verbose_name='Have you seen a doctor in the last year?')
    surgeries = models.CharField(max_length=250, null=True, blank=True, verbose_name='Any Surgeries in the last year?')
    consent_recording = models.ImageField(upload_to='consent_recording/', max_length=100, null=True, blank=True)
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, verbose_name='IP Address')
    submission_id = models.CharField(max_length=350, null=True, blank=True)
    edit_link = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'DME II'
        verbose_name_plural = 'DME II'
        ordering = ['submission_date']

    def __str__(self):
        return str(self.submission_date)
