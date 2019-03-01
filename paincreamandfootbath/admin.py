from django.contrib import admin
from django.utils.html import format_html, mark_safe
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models import PainCreamAndFootBath


class PainCreamAndFootBathProfile(admin.ModelAdmin):
    list_display = ('submission_date', 'patient_first_name', 'patient_last_name',
                    'promo_code', 'insurance_type', 'ppo_hmo_information_mem_id',
                    'ppo_hmo_information_ppo_name')
    list_filter = (
        'state_province', 
        'insurance_status',
        ('submission_date', DateRangeFilter),
        ('date_faxed_to_pharmacy', DateRangeFilter),
        ('date_created', DateRangeFilter),
        )
    search_fields = ['patient_first_name', 'patient_last_name', 'promo_code']
    readonly_fields = ['date_created', 'created_by', 'updated_by', 'user_promo_code',
                       'patient_id_photo_image', 'insurance_card_photo_image', 'ppo_card_photo_image',
                        ]
    fieldsets = (
        (None, {
            'fields': (
                'submission_date',
            )
        }),
        ("Agent Information", {
            'fields': (
                'agent_name',
                'promo_code',
                'agent_email',
            )
        }),
        ("Patient Information", {
            'fields': (
                'patient_first_name',
                'patient_last_name',
                'birth_date',
                'gender',
                'patient_phone_number',
                'best_time_to_call',
                'street_address',
                'street_address_2',
                'city',
                'state_province',
                'postal_zip_code',
                'country',
                'insurance_type',
                'medicare_medicaid_policy',
                'ppo_hmo_information_mem_id',
                'ppo_hmo_information_ppo_name',
                'insurance_status',
                'location_of_pain',
                'level_of_pain',
                'discomfort',
                'feq_of_pain',
                'prescribe_pain_cream',
                'location_of_foot_issue',
                'describe_foot_issue',
                'order_status',
                'date_faxed_to_pharmacy',
                'ip',
                'submission_id'
            )
        }),
        ("Attachments", {
            'fields': (
                'patient_id_photo',
                'patient_id_photo_image',
                'insurance_card_photo',
                'insurance_card_photo_image',
                'ppo_card_photo',
                'ppo_card_photo_image',
                'consent_recording',
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

    def insurance_card_photo_image(self, obj):
        return mark_safe('<img src="{url}" width="145px" height="145px" />'.format(
            url = obj.insurance_card_photo.url,
            width=obj.insurance_card_photo.width,
            height=obj.insurance_card_photo.height,
            )
    )

    def ppo_card_photo_image(self, obj):
        return mark_safe('<img src="{url}" width="145px" height="145px" />'.format(
            url = obj.ppo_card_photo.url,
            width=obj.ppo_card_photo.width,
            height=obj.ppo_card_photo.height,
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


admin.site.register(PainCreamAndFootBath, PainCreamAndFootBathProfile)
