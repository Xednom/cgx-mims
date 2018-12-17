from django.contrib import admin

from .models import Pending, Hold, Rejected, Completed, TypeOfInsurance


class PendingProfile(admin.ModelAdmin):
    list_display = ('name', 'promo_code', 'agent', 'manager', 'state', 'type_of_insurance', 'active_inactive', 'verification_date')
    list_filter = ('status', 'active_inactive', 'state')
    list_per_page = 30
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
