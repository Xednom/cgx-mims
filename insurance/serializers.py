from rest_framework import serializers
from cgx.models import Agent, Manager
from .models import Insurance, TypeOfInsurance


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ('name',)


class TypeOfInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfInsurance
        fields = (
            'name',
            'notes'
        )

class InsuranceSerializer(serializers.ModelSerializer):
    agent = serializers.SlugRelatedField(slug_field='name', queryset=Agent.objects.all())
    manager = serializers.SlugRelatedField(slug_field='name', queryset=Manager.objects.all())
    type_of_insurance = serializers.SlugRelatedField(slug_field='name', queryset=TypeOfInsurance.objects.all())


    class Meta:
        model = Insurance
        fields = '__all__'
