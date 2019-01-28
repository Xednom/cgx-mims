import uuid
import datetime
from django.db import models

from django.utils import timezone
from django.contrib import messages


# type of test choices
CARRIER = 1
CGX = 2
CGX_CARRIER = 3
L = 4

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


TYPE_OF_TEST_CHOICES = (
    (CARRIER, 'CARRIER'),
    (CGX, 'CGX'),
    (CGX_CARRIER, 'CGX/CARRIER'),
    (L, 'L')
)

STATUS_CHOICES = (
    (CGX_CGD, "CGX/CGD"),
    (DUPLICATE, "DUPLICATE"),
    (HOLD, "HOLD"),
    (MISSING_INFORMATION, "MISSING INFORMATION"),
    (REJECTED, "REJECTED"),
    (WRONG_APPLICATION, "WRONG APPLICATION"),
    (RA, "Requires Authorization"),
    (RFE, "Resubmit from Elite"),
    (RESIGNED, "RESIGNED"),
    (REJ_HMO, "REJECTED HMO"),
    (REJ_NO_ID, "REJECTED NO ID"),
    (REJ_INELIGIBLE, "REJECTED INELIGIBLE"),
    (REJ_INACTIVE, "REJECTED INACTIVE"),
    (REJ_HIGD, "REJECTED - Higd ded 6880.37"),
    (REJ_CARESOURCE, "REJECTED CARESOURCE")
)

REASON_FOR_REJECTIONS_CHOICES = (
    (HD, "HIGH DEDUCTIBLE - 2400.00"),
    (HIPAA, "HIPAA VIOLATION"),
    (RRA, "REQUIRES AUTHENTICATION")
)


class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Agent id")
    name = models.CharField(max_length=50, verbose_name="Agent name", null=True, blank=True, unique=True)

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


class BioConfirmMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    for_bioconfirm = models.BooleanField(default=False, verbose_name='For Bio Confirm?')
    patient_name = models.CharField(max_length=250, verbose_name="Patient Name")
    patient_phone_number = models.CharField(max_length=250, verbose_name="Patient phone number", null=True, blank=True)
    promo_code = models.CharField(max_length=250, verbose_name="Promo Code")
    agent = models.ForeignKey(Agent, verbose_name="Agent name", null=True, blank=True, on_delete=models.PROTECT)
    date_app_rec = models.DateField(default=timezone.now, verbose_name="Date application recorded", null=True, blank=True)
    date_sample_rec = models.DateField(default=timezone.now, verbose_name="Date sample recorded", null=True, blank=True)
    type_of_test = models.IntegerField(choices=TYPE_OF_TEST_CHOICES, verbose_name="Test choices", null=True, blank=True)
    date_of_qca = models.DateField(default=timezone.now, verbose_name="Date of QCA", null=True, blank=True)
    submitted_to_tamika_ins_verifier = models.DateField(default=timezone.now, verbose_name="Date submitted to Tamika ins verifier", null=True, blank=True)
    telemed_name = models.CharField(max_length=250, verbose_name="Telemed name", null=True, blank=True)
    date_submitted_to_telemed = models.DateField(default=timezone.now, verbose_name="Date submitted to telemed", null=True, blank=True)
    date_telemed_returned = models.DateField(default=timezone.now, verbose_name="Date telemed returned", null=True, blank=True)
    date_bioconfim_rec_app = models.DateField(default=timezone.now, verbose_name="Date bioconfirm recorded application", null=True, blank=True)
    date_paid = models.DateField(default=timezone.now, verbose_name="Date paid", null=True, blank=True)
    state = models.CharField(max_length=50, verbose_name="State", null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, verbose_name="Status", null=True, blank=True)
    month = models.CharField(max_length=50, null=True, blank=True)
    insurance_company = models.CharField(max_length=50, verbose_name="Insurance company name", null=True, blank=True)
    notes = models.TextField(verbose_name="Notes", null=True, blank=True)
    rejection_date = models.DateField(default=timezone.now, verbose_name="Rejection Date", null=True, blank=True)

    class Meta:
        ordering = ['patient_name']

    def __unicode__(self):
        return self.patient_name

    def __str__(self):
        return self.patient_name

    def save(self):
        if self.for_bioconfirm is False:
            return  # don't save if not True
        else:
            super(BioConfirmMaster, self).save()  # saves if True
