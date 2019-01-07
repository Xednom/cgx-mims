from rest_framework import serializers
from .models import Agent, BioConfirmMaster, Manager


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ('name',)


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = ('name',)


class BioConfirmMasterSerializer(serializers.ModelSerializer):
    agent = serializers.SlugRelatedField(slug_field='name', queryset=Agent.objects.all())

    class Meta:
        model = BioConfirmMaster
        fields = '__all__'
