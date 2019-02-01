from django.contrib import admin
from django.utils.html import format_html, mark_safe

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
    readonly_fields = ['patient_id_photo_image', 'insurance_card_photo_front_image',
                       'insurance_card_photo_back_image',
                       'additional_insurance_cards_image', 'consent_recording_image']
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
        }),
        ("Attachments", {
            'fields': (
                'patient_id_photo',
                'patient_id_photo_image',
                'insurance_card_photo_front',
                'insurance_card_photo_front_image',
                'insurance_card_photo_back',
                'insurance_card_photo_back_image',
                'additional_insurance_cards',
                'additional_insurance_cards_image',
                'consent_recording',
                'consent_recording_image',
            )
        })
    )

    def patient_id_photo_image(self, obj):
        return mark_safe('<img src="{url}" width="145px" height="145px" />'.format(
            url = obj.patient_id_photo.url,
            width = obj.patient_id_photo.width,
            height = obj.patient_id_photo.height,
            )
    )

    def insurance_card_photo_front_image(self, obj):
        return mark_safe('<img src="{url}" width="145px" height="145px" />'.format(
            url = obj.insurance_card_photo_front.url,
            width=obj.insurance_card_photo_front.width,
            height=obj.insurance_card_photo_front.height,
            )
    )

    def insurance_card_photo_back_image(self, obj):
        return mark_safe('<img src="{url}" width="145px" height="145px" />'.format(
            url = obj.insurance_card_photo_back.url,
            width=obj.insurance_card_photo_back.width,
            height=obj.insurance_card_photo_back.height,
            )
    )

    def additional_insurance_cards_image(self, obj):
        return mark_safe('<img src="{url}" width="145px" height="145px" />'.format(
            url = obj.additional_insurance_cards.url,
            width=obj.additional_insurance_cards.width,
            height=obj.additional_insurance_cards.height,
            )
    )

    def consent_recording_image(self, obj):
        return mark_safe('<img src="{url}" width="145px" height="145px" />'.format(
            url = obj.consent_recording.url,
            width=obj.consent_recording.width,
            height=obj.consent_recording.height,
            )
    )


admin.site.register(Insurance, InsuranceProfile)
admin.site.register(TypeOfInsurance)
