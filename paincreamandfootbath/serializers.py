import datetime

from rest_framework import serializers
from .models import PainCreamAndFootBath

from cgx.models import Agent


class PainCreamAndFootBathSerializer(serializers.ModelSerializer):
    agent_name = serializers.SlugRelatedField(slug_field='name', queryset=Agent.objects.all())
    date_created = serializers.DateTimeField(default=datetime.datetime.today)

    class Meta:
        model = PainCreamAndFootBath
        fields = '__all__'
