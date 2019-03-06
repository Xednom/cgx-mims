from django.contrib import admin
from django.utils.html import format_html, mark_safe
# from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from jet.filters import DateRangeFilter

from .models import Carrier


class CarrierProfile(admin.ModelAdmin):
    list_display = ('patient_name', 'promo_code', 'agent', 'manager',
                    'date_submitted_to_telemed', 'date_telemed_returned',
                    'date_app_rec', 'date_sample_rec', 'date_of_qca', 'date_paid',
                    'insurance_company', 'rejection_date',
                    'insurance_verified_tsg_verification',)
    list_filter = (
        'status', 
        'month', 
        'state', 
        'type_of_test',
        ('date_created', DateRangeFilter),
        ('date_app_rec', DateRangeFilter),
        ('date_sample_rec', DateRangeFilter),
        ('date_of_qca', DateRangeFilter),
        )
    list_per_page = 30
    #change_list_template = 'carrier/change_list_graph.html'
    search_fields = ('patient_name', 'promo_code', 'agent')
    readonly_fields = ('date_created', 'created_by', 'updated_by', 'user_promo_code', 'patient_id_photo_image',
                        'insurance_card_photo_front_image', 'insurance_card_photo_back_image',
                       'additional_insurance_cards_image', 'consent_recording_image'
                       )
    fieldsets = (
        ('Patient Informations', {
            'fields': (
                'patient_name',
                'patient_phone_number',
                'promo_code',
                'agent',
                'manager',
                'type_of_test',
                'insurance_verified_tsg_verification',
                'telemed_name',
                'state',
                'status',
                'lab_type',
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
                'date_lab_recorded_app',
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
        ("Important informations", {
            'fields': (
                'date_created',
                'created_by',
                'updated_by',
                'user_promo_code',
            )
        })
    )

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, save the user who will add this
            obj.created_by = request.user.first_name + " " + request.user.last_name
            obj.user_promo_code = request.user.agent_promo_code
        elif change:
            obj.updated_by = request.user.first_name + " " + request.user.last_name
        obj.save()

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

    class Media:
        css = {
            'all': ('css/admin/widgets.css',)
        }



admin.site.register(Carrier, CarrierProfile)
