import datetime

from rest_framework import serializers
from .models import DME_II

from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr


class DMEIISerializer(serializers.ModelSerializer):

    patient_id_photo = serializers.ImageField(max_length=None, use_url=True, required=False)
    submission_date = serializers.DateField(default=datetime.date.today)

    class Meta:
        model = DME_II
        fields = '__all__'
