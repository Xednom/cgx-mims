import datetime

from rest_framework import serializers
from .models import Agent, BioConfirmMaster, Manager, Test_choices, Status


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ('name',)


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = ('name',)


class TestChoicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test_choices
        fields = ('name',)


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('name',)


class BioConfirmMasterSerializer(serializers.ModelSerializer):
    agent = serializers.SlugRelatedField(slug_field='name', queryset=Agent.objects.all())
    manager = serializers.SlugRelatedField(slug_field='name', queryset=Manager.objects.all())
    type_of_test = serializers.SlugRelatedField(slug_field='name', queryset=Test_choices.objects.all(), required=False)
    status = serializers.SlugRelatedField(slug_field='name', queryset=Status.objects.all(), required=False)
    date_app_rec = serializers.DateField(default=datetime.date.today)

    class Meta:
        model = BioConfirmMaster
        fields = '__all__'
