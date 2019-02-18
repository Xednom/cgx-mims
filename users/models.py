from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # additional fields in here
    date_of_birth = models.DateField(null=True, blank=True)
    agent_promo_code = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
