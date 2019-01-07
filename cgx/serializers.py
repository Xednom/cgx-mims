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
        fields = (
            'id',
            'patient_name',
            'patient_phone_number',
            'promo_code',
            'agent',
            'date_app_rec',
            'date_sample_rec',
            'type_of_test',
            'date_of_qca',
            'submitted_to_tamika_ins_verifier',
            'telemed_name',
            'date_submitted_to_telemed',
            'date_telemed_returned',
            'date_bioconfim_rec_app',
            'date_paid',
            'state',
            'status',
            'month',
            'insurance_company',
            'notes',
            'rejection_date'
        )
