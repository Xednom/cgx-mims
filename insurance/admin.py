from django.contrib import admin

from .models import Pending, Hold, Rejected, Completed, TypeOfInsurance


class PendingProfile(admin.ModelAdmin):
    list_display = ('name', 'promo_code', 'agent', 'manager', 'state', 'type_of_insurance', 'active_inactive', 'verification_date')
    list_filter = ('status', 'active_inactive', 'state')
    list_per_page = 30
    change_list_template = 'insurance/pending_change_list_graph.html'
    fieldsets = (
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


class HoldProfile(admin.ModelAdmin):
    list_display = ('name', 'promo_code', 'agent', 'manager', 'state', 'type_of_insurance', 'active_inactive', 'verification_date')
    list_filter = ('status', 'active_inactive', 'state')
    list_per_page = 30
    change_list_template = 'insurance/hold_change_list_graph.html'
    fieldsets = (
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


class RejectedProfile(admin.ModelAdmin):
    list_display = ('name', 'promo_code', 'agent', 'manager', 'state', 'type_of_insurance', 'active_inactive', 'verification_date')
    list_filter = ('status', 'active_inactive', 'state')
    list_per_page = 30
    change_list_template = 'insurance/rejected_change_list_graph.html'
    fieldsets = (
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


class CompletedProfile(admin.ModelAdmin):
    list_display = ('name', 'promo_code', 'agent', 'manager', 'state', 'type_of_insurance', 'active_inactive', 'verification_date')
    list_filter = ('status', 'active_inactive', 'state')
    list_per_page = 30
    change_list_template = 'insurance/completed_change_list_graph.html'
    fieldsets = (
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


admin.site.register(Pending, PendingProfile)
admin.site.register(Hold, HoldProfile)
admin.site.register(Rejected, RejectedProfile)
admin.site.register(Completed, CompletedProfile)
admin.site.register(TypeOfInsurance)
