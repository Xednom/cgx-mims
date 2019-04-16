import uuid
import datetime
from django.db import models

from django.utils import timezone
from django.contrib import messages


# type of test choices
CARRIER = "CARRIER"
CGX = "CGX"
CGX_CARRIER = "CGX/CARRIER"
L = "L"

# STATUS_CHOICES
CGX_CGD = "CGX/CGD"
DUPLICATE = "DUPLICATE"
HOLD = "HOLD"
MISSING_INFORMATION = "MISSING INFORMATION"
REJECTED = "REJECTED"
WRONG_APPLICATION = "WRONG APPLICATION"
RFE = "Resubmit from Elite"
RESIGNED = "RESIGNED"
RA = "Requires Authorization"
REJ_HMO = "REJECTED HMO"
REJ_NO_ID = "REJECTED NO ID"
REJ_INELIGIBLE = "REJECTED INELIGIBLE"
REJ_INACTIVE = "REJECTED INACTIVE"
REJ_HIGD = "REJECTED - Higd ded 6880.37"
REJ_CARESOURCE = "REJECTED CARESOURCE"

# REASON_FOR_REJECTIONS_CHOICES
HD = 1
HIPAA = 2
RRA = 3

REASON_FOR_REJECTIONS_CHOICES = (
    (HD, "HIGH DEDUCTIBLE - 2400.00"),
    (HIPAA, "HIPAA VIOLATION"),
    (RRA, "REQUIRES AUTHENTICATION")
)


class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Agent id")
    name = models.CharField(max_length=50, verbose_name="Agent name", null=True, blank=True, unique=True)
    promo_code = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Agent name'
        verbose_name_plural = 'Agent names'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Manager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Manager id")
    name = models.CharField(max_length=50, verbose_name="Manager name", null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Manager name'
        verbose_name_plural = 'Manager names'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Status id')
    name = models.CharField(max_length=250, verbose_name='Status', null=True, blank=True)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        ordering=['name']

    def __str__(self):
        return str(self.name)


class Test_choices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Test choices id')
    name = models.CharField(max_length=250, verbose_name="Test choice", null=True, blank=True)

    class Meta:
        verbose_name = 'Test Choice'
        verbose_name_plural = 'Test Choices'
        ordering=['name']

    def __str__(self):
        return str(self.name)


class BioConfirmMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_name = models.CharField(max_length=250, verbose_name="Patient Name", null=True, blank=True, unique=True)
    patient_phone_number = models.CharField(max_length=250, verbose_name="Patient phone number", null=True, blank=True)
    promo_code = models.CharField(max_length=250, verbose_name="Promo Code", null=True, blank=True)
    agent = models.ForeignKey(Agent, verbose_name="Agent name", null=True, blank=True, on_delete=models.PROTECT)
    manager = models.ForeignKey(Manager, verbose_name="Manager name", null=True, blank=True, on_delete=models.PROTECT)
    date_app_rec = models.DateField(default=timezone.now, verbose_name="Date application recorded", null=True, blank=True)
    date_sample_rec = models.DateField(verbose_name="Date sample recorded", null=True, blank=True)
    type_of_test = models.ForeignKey(Test_choices, max_length=250, verbose_name="Test choices", null=True, blank=True, on_delete=models.PROTECT)
    date_of_qca = models.DateField(verbose_name="Date of QCA", null=True, blank=True)
    insurance_verified_tsg_verification = models.DateField(verbose_name="Insurance Verified/TSG Verification", null=True, blank=True)
    telemed_name = models.CharField(max_length=250, verbose_name="Telemed name", null=True, blank=True)
    date_submitted_to_telemed = models.DateField(verbose_name="Date submitted to telemed", null=True, blank=True)
    date_telemed_returned = models.DateField(verbose_name="Date telemed returned", null=True, blank=True)
    date_bioconfim_rec_app = models.DateField(verbose_name="Date bioconfirm recorded application", null=True, blank=True)
    date_paid = models.DateField(verbose_name="Date paid", null=True, blank=True)
    date_lab_recorded_app = models.DateField(null=True, blank=True)
    lab_type = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=50, verbose_name="State", null=True, blank=True)
    status = models.ForeignKey(Status, max_length=250, verbose_name="Status", null=True, blank=True, on_delete=models.PROTECT)
    month = models.CharField(max_length=50, null=True, blank=True)
    insurance_company = models.CharField(max_length=50, verbose_name="Insurance company name", null=True, blank=True)
    notes = models.TextField(verbose_name="Notes", null=True, blank=True)
    rejection_date = models.DateField(verbose_name="Rejection Date", null=True, blank=True)
    patient_id_photo = models.ImageField(upload_to='bio-confirm-master/patient-id-photo/', max_length=1000, null=True, blank=True)
    insurance_card_photo_front = models.ImageField(upload_to='bio-confirm-master/insurance-card-photo-front/', max_length=1000, null=True, blank=True)
    insurance_card_photo_back = models.ImageField(upload_to='bio-confirm-master/insurance-card-photo-back/', max_length=1000, null=True, blank=True)
    additional_insurance_cards = models.ImageField(upload_to='bio-confirm-master/additional-insurance-cards/', max_length=1000, null=True, blank=True)
    consent_recording = models.FileField(upload_to='bio-confirm-master/consent-recording/', max_length=1000, null=True, blank=True)
    date_created = models.DateField(default=datetime.date.today, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    user_promo_code = models.CharField(max_length=100, verbose_name="Promo code of the agent who created this record.", null=True, blank=True)

    class Meta:
        ordering = ['patient_name']

    def __str__(self):
        return str(self.patient_name)
