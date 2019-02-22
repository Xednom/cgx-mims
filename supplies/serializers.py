from rest_framework import serializers
from .models import Supply


class SuppliesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = '__all__'