import uuid

from django.db import models


class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Agent_id")
    name = models.CharField(max_length=50, verbose_name="Agent_name")


class Manager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Manager_id")
    name = models.CharField(max_length=50, verbose_name="Manager_name")




