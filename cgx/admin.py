from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html, mark_safe

from django.contrib import admin

from .models import Agent, Manager, BioConfirmMaster


class BioConfirmMasterProfile(admin.ModelAdmin):
    list_display = ('patient_name', 'promo_code', 'agent',
                    'date_submitted_to_telemed', 'date_telemed_returned',
                    'date_app_rec', 'date_sample_rec', 'date_paid',
                    'insurance_company', 'rejection_date',
                    'submitted_to_tamika_ins_verifier')
    list_filter = ('month', 'state', 'type_of_test')
    list_per_page = 30
    change_list_template = 'cgx/change_list_graph.html'
    search_fields = ('patient_name', 'promo_code', 'agent')
    readonly_fields = ['patient_id_photo_image', 'insurance_card_photo_front_image',
                       'insurance_card_photo_back_image',
                       'additional_insurance_cards_image', 'consent_recording_image']
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
        }),
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


# admin.site.register(BioConfirmMaster, BioConfirmMasterProfile)


@admin.register(BioConfirmMaster)
class BioConfirmMasterAdmin(ImportExportModelAdmin, BioConfirmMasterProfile):
    actions = None
    # inlines = [BioConfirmMasterStatusInline]


admin.site.register(Agent)
admin.site.register(Manager)
