from django.contrib import admin
from django.utils.html import format_html, mark_safe

from .models import DME_II


class DMEIIProfile(admin.ModelAdmin):
    list_display = ['submission_date', 'patients_first_name',
                    'patients_last_name', 'agents_promod_code', 'insurance_type',
                    'policy_number', 'ppo_information_mem_id',
                    'ppo_information_ppo_name']
    list_filter = ['state_province', 'insurance_status', 'insurance_notes']
    search_filters = ['first_name', 'last_name', 'agents_promod_code']
    readonly_fields = [
                       'date_created', 'created_by', 'updated_by', 'user_promo_code',
                       'patient_id_photo_image', 'insurance_card_photo_front_image',
                       'insurance_card_photo_back_image', 'additional_insurance_cards_image',
                        'consent_recording_image'
                      ]
    fieldsets = (
        (None, {
            'fields': (
                'submission_date',
            )
        }),
        ("Agent Information", {
            'fields': (
                'first_name',
                'last_name',
                'agents_promod_code',
                'agents_email',
            )
        }),
        ("Patient's Information", {
            'fields': (
                'patients_first_name',
                'patients_last_name',
                'birth_date',
                'gender',
                'patients_phone_number',
                'best_time_to_call',
                'street_address',
                'street_address_line_2',
                'city',
                'state_province',
                'postal_zip_code',
                'country',
                'insurance_type',
                'policy_number',
                'ppo_information_mem_id',
                'ppo_information_ppo_name',
                'insurance_status',
                'insurance_notes',
                'location_of_back_pain',
                'location_of_shoulder_pain',
                'location_of_knee_pain',
                'location_of_elbow_pain',
                'localtion_of_wrist_pain',
                'height',
                'weight',
                'size_of_brace',
            )
        }),
        ("Medical Information", {
            'fields': (
                'major_medical_conditions',
                'cause_of_pain_discomfort',
                'level_of_pain',
                'experiencing_discomfort',
                'frequency_of_pain',
                'describe_pain',
                'pain_symptoms',
                'pain_worse',
                'treatments_tried',
                'seen_doctor',
                'surgeries',
                'ip',
                'submission_id',
                'edit_link'
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
        ("Important Informations", {
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


admin.site.register(DME_II, DMEIIProfile)
