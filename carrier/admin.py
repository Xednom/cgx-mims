from django.contrib import admin

from .models import Carrier


class CarrierProfile(admin.ModelAdmin):
    list_display = ('patient_name', 'promo_code', 'agent',
                    'date_submitted_to_telemed', 'date_telemed_returned',
                    'date_app_rec', 'date_sample_rec', 'date_paid',
                    'insurance_company', 'rejection_date',
                    'submitted_to_tamika_ins_verifier')
    list_filter = ('status', 'month', 'state', 'type_of_test')
    list_per_page = 30
    change_list_template = 'carrier/change_list_graph.html'
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


admin.site.register(Carrier, CarrierProfile)
