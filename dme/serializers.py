from rest_framework import serializers
from .models import DME_II


class DMEIISerializer(serializers.ModelSerializer):

    class Meta:
        model = DME_II
        fields = '__all__'
