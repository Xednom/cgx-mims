import uuid
import datetime
from django.db import models


CARRIER = 1
CGX = 2
CGX_CARRIER = 3
L = 4

CGX_CGD = 1
DUPLICATE = 2
HOLD = 3
MISSING_INFORMATION = 4
REJECTED = 5
WRONG_APPLICATION = 6
RFE = 7
RESIGNED = 8
RA = 9
REJ_HMO = 10
REJ_NO_ID = 11
REJ_INELIGIBLE = 12
REJ_INACTIVE = 13
REJ_HIGD = 14
REJ_CARESOURCE = 15

HD = 1
HIPAA = 2
RA = 3


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
    (RFE, "Resubmit from Elite"),
    (RESIGNED, "RESIGNED"),
    (REJ_HMO, "REJECTED - HMO"),
    (REJ_NO_ID, "REJECTED - NO ID"),
    (REJ_INELIGIBLE, "REJECTED - INELIGIBLE"),
    (REJ_INACTIVE, "REJECTED - INACTIVE"),
    (REJ_HIGD, "Higd ded 6680.37"),
    (REJ_CARESOURCE, "REJECTED - CARESOURCE")
)

REASON_FOR_REJECTIONS_CHOICES = (
    (HD, "HIGH DEDUCTIBLE - 2400.00"),
    (HIPAA, "HIPAA VIOLATION"),
    (RA, "REQUIRES AUTHENTICATION")
)


class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Agent id")
    name = models.CharField(max_length=50, verbose_name="Agent_name")


class Manager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Manager id")
    name = models.CharField(max_length=50, verbose_name="Manager name")


class BioConfirmMaster(models.Model):
    patient_name = models.CharField(max_length=50, verbose_name="patient name")
    patient_phone_number = models.CharField(max_length=50, verbose_name="patient phone number")
    promo_code = models.CharField(max_length=50, verbose_name="promo code")
    agent = models.ForeignKey(Agent)
    date_app_rec = models.DateField(default=datetime.date.today(), verbose_name="date application recorded")
    date_sample_rec = models.DateField(default=datetime.date.today(), verbose_name="date sample recorded")
    type_of_test = models.IntegerField(choices=TYPE_OF_TEST_CHOICES, verbose_name="test choices")
    date_of_qca = models.DateField(default=datetime.date.today(), verbose_name="date of qca")
    submitted_to_tamika_ins_verifier = models.DateField(default=datetime.date.today(),
                                                        verbose_name="Date submitted to tamika ins verifier")
    telemed_name = models.CharField(max_length=50, verbose_name="Telemed name")
    date_submitted_to_telemed = models.DateField(default=datetime.date.today(),
                                                 verbose_name="date submitted to telemed")
    date_telemed_returned = models.DateField(default=datetime.date.today(), verbose_name="date telemed returned")
    date_bioconfim_rec_app = models.DateField(default=datetime.date.today(),
                                              verbose_name="date bioconfirm recorded application")
    date_paid = models.DateField(default=datetime.date.today(), verbose_name="date paid")
    state = models.CharField(max_length=50, verbose_name="state")
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name="status")
    month = models.CharField(max_length=10, verbose_name="month")
    insurance_company = models.CharField(max_length=50, verbose_name="insurance company")
    notes = models.TextField(blank=True, null=True, verbose_name="notes")
    rejection_date = models.DateField(default=datetime.date.today(), verbose_name="Rejection Date")


