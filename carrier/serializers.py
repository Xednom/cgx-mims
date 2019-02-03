import datetime
from rest_framework import serializers

from .models import Carrier
from cgx.models import Agent


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ('name',)


class CarrierSerializer(serializers.ModelSerializer):
    agent = serializers.SlugRelatedField(slug_field='name', queryset=Agent.objects.all())
    date_paid = serializers.DateField(default=datetime.date.today)
    date_of_qca = serializers.DateField(default=datetime.date.today)
    date_app_rec = serializers.DateField(default=datetime.date.today)
    date_sample_rec = serializers.DateField(default=datetime.date.today)
    date_telemed_returned = serializers.DateField(default=datetime.date.today)
    date_bioconfim_rec_app = serializers.DateField(default=datetime.date.today)
    date_submitted_to_telemed = serializers.DateField(default=datetime.date.today)
    rejection_date = serializers.DateField(default=datetime.date.today)

    class Meta:
        model = Carrier
        fields = '__all__'
