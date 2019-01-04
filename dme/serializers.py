from rest_framework import serializers
from .models import DME
from cgx.models import Manager


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = ('name',)


class DMESerializer(serializers.ModelSerializer):
    manager_name = serializers.SlugRelatedField(slug_field='name', queryset=Manager.objects.all())

    class Meta:
        model = DME
        fields = (
            'id',
            'agent_id',
            'manager_name',
            'patient_id',
            'date',
            'sent_to_telemed',
            'patient_status',
            'date_returned_for_refiling_with_remn',
            'eligibility_verified',
            'patient_first_name',
            'patient_last_name',
            'primary_insurance_name',
            'braces_requested',
            'braces_s_plus_s_approved',
            'braces_shipped',
            'notes',
            'created_at',
            'updated_at',
            'who_updated'
        )














