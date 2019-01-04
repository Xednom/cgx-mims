from rest_framework import serializers
from cgx.models import Agent, Manager
from .models import Insurance, TypeOfInsurance


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

    class Meta:
        model = Insurance
        fields = (
            'id',
            'name',
            'promo_code',
            'agent',
            'manager',
            'date_of_birth',
            'state',
            'type_of_insurance',
            'test',
            'active_inactive',
            'status',
            'insurance_status',
            'policy_number',
            'verification_date',
            'deductible_remainding',
            'notes'
        )







