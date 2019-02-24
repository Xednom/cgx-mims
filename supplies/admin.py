from django.contrib import admin

from .models import Supply


class SuppliesProfile(admin.ModelAdmin):
    list_display = ('sale_rep_name', 'sale_rep_number', 'email')
    search_fields = ('sale_rep_name', 'sale_rep_number', 'email')
    fieldsets = (
        ("Shipping", {
            'fields': (
                'shipping_labels_qty_req',
                'shipping_labels_qty_auth',
                'shipping_boxes_qty_req',
                'shipping_boxes_qty_auth',
                'shipping_bags_qty_req',
                'shipping_bags_qty_auth',
                'specimen_bags_qty_req',
                'specimen_bags_qty_auth',
            )
        }),
        ("Tox", {
            'fields': (
                'tox_cups_qty_req',
                'tox_cups_qty_auth',
                'tox_req_forms_qty_req',
                'tox_req_forms_qty_auth',
            )
        }),
        ("PGX", {
            'fields': (
                'pgx_swabs_qty_req',
                'pgx_swabs_qty_auth',
                'pgx_swabs_req_forms_qty_req',
                'pgx_swabs_req_forms_qty_auth',
                'pgx_medical_necessity_forms_qty_req',
                'pgx_medical_necessity_forms_qty_auth',
            )
        }),
        ("CGX", {
            'fields': (
                'cgx_swabs_qty_req',
                'cgx_swabs_qty_auth',
            )
        }),
        ("Tubes", {
            'fields': (
                'tubes_tiger_qty_req',
                'tubes_tiger_qty_auth',
                'tubes_lavender_qty_req',
                'tubes_lavender_qty_auth',
                'tubes_red_top_qty_req',
                'tubes_red_top_qty_auth',
                'tubes_blue_qty_req',
                'tubes_blue_qty_auth',
                'tubes_dark_blue_qty_req',
                'tubes_dark_blue_qty_auth',
                'tubes_violet_qty_req',
                'tubes_violet_qty_auth',
            )
        }),
        ("Needles", {
            'fields': (
                'straight_needle_18_qty_req',
                'straight_needle_18_qty_auth',
                'straight_needle_20_qty_req',
                'straight_needle_20_qty_auth',
                'straight_needle_21_qty_req',
                'straight_needle_21_qty_auth',
                'straight_needle_22_qty_req',
                'straight_needle_22_qty_auth',
                'straight_needle_23_qty_req',
                'straight_needle_23_qty_auth',
                'butterfly_needle_18_qty_req',
                'butterfly_needle_18_qty_auth',
                'butterfly_needle_20_qty_req',
                'butterfly_needle_20_qty_auth',
                'butterfly_needle_21_qty_req',
                'butterfly_needle_21_qty_auth',
                'butterfly_needle_22_qty_req',
                'butterfly_needle_22_qty_auth',
                'butterfly_needle_23_qty_req',
                'butterfly_needle_23_qty_auth',
                'needle_vacuum_tubes_18_qty_req',
                'needle_vacuum_tubes_18_qty_auth',
            )
        }),
        ("UTI", {
            'fields': (
                'uti_cups_qty_req',
                'uti_cups_qty_auth',
                'uti_urine_tubes_qty_req',
                'uti_urine_tubes_qty_auth',
            )
        }),
        ("Miscellaneous", {
            'fields': (
                'culture_swabs_qty_req',
                'culture_swabs_qty_auth',
                'tourniquets_qty_req',
                'tourniquets_qty_auth',
                'gauze_qty_req',
                'gauze_qty_auth',
                'bandages_qty_req',
                'bandages_qty_auth',
                'gel_pack_qty_req',
                'gel_pack_qty_auth',
            )
        })
    )


admin.site.register(Supply, SuppliesProfile)
