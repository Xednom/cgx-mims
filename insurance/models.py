import uuid
import datetime
from django.db import models

from django.utils import timezone

from cgx.models import Agent, Manager

# type of test choices
CARRIER = 1
CGX = 2
CGX_CARRIER = 3

TYPE_OF_TEST_CHOICES = (
    (CARRIER, 'Carrier'),
    (CGX, 'CGX'),
    (CGX_CARRIER, 'CGX/Carrier')
)


class TypeOfInsurance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, verbose_name='Name of the Insurance')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Insurance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, unique=True, verbose_name='Patient Name')
    promo_code = models.CharField(max_length=250, verbose_name='Promo Code', null=True, blank=True)
    agent = models.ForeignKey(Agent, verbose_name='Agent name', on_delete=models.PROTECT, null=True, blank=True)
    manager = models.ForeignKey(Manager, verbose_name='Manager Name', on_delete=models.PROTECT, null=True, blank=True)
    date_of_birth = models.DateField(default=datetime.date.today, verbose_name='Date of Birth', null= True, blank=True)
    state = models.CharField(max_length=250, verbose_name='State', null=True, blank=True)
    type_of_insurance = models.ForeignKey(TypeOfInsurance, verbose_name='Type of Insurance', on_delete=models.PROTECT, null=True, blank=True)
    test = models.CharField(max_length=250, verbose_name='Test',  null=True, blank=True)
    active_inactive = models.CharField(max_length=250, verbose_name='Active/Inactive', null=True, blank=True)
    status = models.CharField(max_length=150, verbose_name='Status', null=True, blank=True)
    insurance_status = models.CharField(max_length=200, verbose_name='Insurance Status', null=True, blank=True)
    policy_number = models.CharField(max_length=250, verbose_name='Policy Number', null=True, blank=True)
    verification_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    deductible_remainding = models.CharField(max_length=250, verbose_name='Deductible Remainding', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    patient_id_photo = models.ImageField(upload_to='insurance/patient-id-photo/', max_length=1000, null=True, blank=True)
    insurance_card_photo_front = models.ImageField(upload_to='insurance/insurance-card-photo-front/', max_length=1000, null=True, blank=True)
    insurance_card_photo_back = models.ImageField(upload_to='insurance/insurance-card-photo-back/', max_length=1000, null=True, blank=True)
    additional_insurance_cards = models.ImageField(upload_to='insurance/additional-insurance-cards/', max_length=1000, null=True, blank=True)
    consent_recording = models.FileField(upload_to='insurance/consent_recording/', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Insurance records'
        ordering = ['name']

    def __str__(self):
        return self.name
