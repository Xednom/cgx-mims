from rest_framework import serializers

from .models import Carrier
from cgx.models import Agent


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ('name',)


class CarrierSerializer(serializers.ModelSerializer):
    agent = serializers.SlugRelatedField(slug_field='name', queryset=Agent.objects.all())

    class Meta:
        model = Carrier
        fields = '__all__'
