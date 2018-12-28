import uuid
import datetime
from django.db import models

from django.utils import timezone

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


class DME(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent_id = models.CharField(max_length=250, verbose_name='Agent ID Number')
    manager_name = models.ForeignKey(Manager, verbose_name='Manager Name', on_delete=models.PROTECT, null=True, blank=True)
    patient_id = models.CharField(max_length=250, verbose_name='Patient ID Number', null=True, blank=True)
    date = models.DateField(default=timezone.now, verbose_name='Date', null=True, blank=True)
    sent_to_telemed = models.CharField(max_length=250, verbose_name='Sent to Telemed', null=True, blank=True)
    patient_status = models.CharField(max_length=2, choices=PATIENT_STATUS_CHOICES, null=True, blank=True)
    date_returned_for_refiling_with_remn = models.DateField(timezone.now, null=True, blank=True)
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
