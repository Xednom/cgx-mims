from django.contrib import admin

from .models import DME


class DMEProfile(admin.ModelAdmin):
    list_display = ('agent_id', 'patient_first_name', 'patient_last_name', 'patient_id', 'patient_status')
    list_filter = ('patient_status',)
    list_per_page = 30
    search_filters = ('agent_id', 'patient_id', 'patient_last_name', 'patient_first_name')
    fieldsets = (
        ("Patient's Informations", {
            'fields': (
                'agent_id',
                'manager_name',
                'patient_id',
                'sent_to_telemed',
                'patient_status',
                'eligibility_verified',
                'patient_first_name',
                'patient_last_name',
                'primary_insurance_name',
                'braces_requested',
                'braces_s_plus_s_approved',
                'braces_shipped',
                'notes'
            )
        }),
        ("Date informations on Patient's", {
            'fields': (
                'date',
                'date_returned_for_refiling_with_remn',
                'created_at',
                'updated_at',
                'who_updated'
            )
        })
    )


admin.site.register(DME, DMEProfile)
