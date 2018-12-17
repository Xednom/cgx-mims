from django.contrib import admin

from .models import Agent, Manager, BioConfirmMaster


class BioConfirmMasterProfile(admin.ModelAdmin):
    list_display = ('patient_name', 'promo_code', 'agent', 'date_app_rec', 'date_sample_rec')
    list_filter = ('status',)
    list_per_page = 30
    change_list_template = 'cgx/change_list_graph.html'
    search_fields = ('patient_name', 'promo_code', 'agent')
    fieldsets = (
        ('Patient Informations', {
            'fields': (
                'patient_name',
                'patient_phone_number',
                'promo_code',
                'agent',
                'type_of_test',
                'submitted_to_tamika_ins_verifier',
                'telemed_name',
                'state',
                'status',
                'insurance_company',
                'notes'
            )
        }),
        ("Patient's date informations", {
            'fields': (
                'date_app_rec',
                'date_sample_rec',
                'date_of_qca',
                'date_submitted_to_telemed',
                'date_telemed_returned',
                'date_bioconfim_rec_app',
                'date_paid',
                'month',
                'rejection_date',
            )
        })
    )


admin.site.register(BioConfirmMaster, BioConfirmMasterProfile)
admin.site.register(Agent)
admin.site.register(Manager)
