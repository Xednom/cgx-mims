from django.contrib import admin

from .models import Insurance, TypeOfInsurance


class InsuranceProfile(admin.ModelAdmin):
    list_display = ('name', 'promo_code', 'agent', 'manager', 'state',
                    'type_of_insurance', 'test', 'active_inactive', 'status',
                    'insurance_status', 'policy_number', 'verification_date',
                    'deductible_remainding', 'notes')
    list_filter = ('status', 'active_inactive', 'state')
    list_per_page = 30
    search_filters = ('name', 'promo_code', 'agent', 'manager', 'policy_number')
    change_list_template = 'insurance/change_list_graph.html'
    fieldsets = (
        ("Confirmation if this information is for Insurance", {
            'fields': (
                'for_insurance',
            )
        }),
        ('Insurance Informations', {
            'fields': (
                'name',
                'promo_code',
                'agent',
                'manager',
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
        }),
        ("Patient's personal Informations", {
            'fields': (
                'date_of_birth',
            )
        })
    )


admin.site.register(Insurance, InsuranceProfile)
admin.site.register(TypeOfInsurance)
