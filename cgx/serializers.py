import datetime

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
    date_paid = serializers.DateField(default=datetime.date.today)
    date_of_qca = serializers.DateField(default=datetime.date.today)
    date_app_rec = serializers.DateField(default=datetime.date.today)
    date_sample_rec = serializers.DateField(default=datetime.date.today)
    date_telemed_returned = serializers.DateField(default=datetime.date.today)
    date_bioconfim_rec_app = serializers.DateField(default=datetime.date.today)
    date_submitted_to_telemed = serializers.DateField(default=datetime.date.today)
    rejection_date = serializers.DateField(default=datetime.date.today)
    date_created = serializers.DateField(default=datetime.date.today)

    class Meta:
        model = BioConfirmMaster
        fields = '__all__'
