import uuid
from django.db import models


class Supply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale_rep_name = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    sale_rep_number = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    shipping_labels_qty_req = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    shipping_labels_qty_auth = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    shipping_boxes_qty_req = models.CharField(max_length=250, default='n/a',
                                              verbose_name='Boxes Quantity Req', null=True, blank=True)
    shipping_boxes_qty_auth = models.CharField(max_length=250, default='n/a',
                                              verbose_name='Boxes Quantyty Auth', null=True, blank=True)
    shipping_bags_qty_req = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    shipping_bags_qty_auth = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    specimen_bags_qty_req = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    specimen_bags_qty_auth = models.CharField(max_length=250, default='n/a', null=True, blank=True)
    tox_cups_qty_req = models.CharField(max_length=250, default='n/a',
                                        verbose_name='Cups Quantity Req', null=True, blank=True)
    tox_cups_qty_auth = models.CharField(max_length=250, default='n/a',
                                        verbose_name='Tox Cups Quanty Auth', null=True, blank=True)
    tox_req_forms_qty_req = models.CharField(max_length=250, default='n/a',
                                             verbose_name='Tox Req. Forms Qty Req.', null=True, blank=True)
    tox_req_forms_qty_auth = models.CharField(max_length=250, default='n/a',
                                             verbose_name='Tox Req. Forms Qty Auth.', null=True, blank=True)
    pgx_swabs_qty_req = models.CharField(max_length=250, default='n/a',
                                        verbose_name='PGX Swabs Qty Req.', null=True, blank=True)
    pgx_swabs_qty_auth = models.CharField(max_length=250, default='n/a',
                                         verbose_name='PGX Swabs Qty Auth.', null=True, blank=True)
    pgx_swabs_req_forms_qty_req = models.CharField(max_length=250, default='n/a',
                                         verbose_name='PGX Swabs Req. Forms Qty Req.', null=True, blank=True)
    pgx_swabs_req_forms_qty_auth = models.CharField(max_length=250, default='n/a',
                                         verbose_name='PGX Swabs Req. Forms Qty Auth.', null=True, blank=True)
    pgx_medical_necessity_forms_qty_req = models.CharField(max_length=250, default='n/a',
                                         verbose_name='PGX Swabs Medical Necessity Forms Qty Req.', null=True, blank=True)
    pgx_medical_necessity_forms_qty_auth = models.CharField(max_length=250, default='n/a',
                                                           verbose_name='PGX Swabs Medical Necessity Forms Qty Auth.', null=True, blank=True)
    cgx_swabs_qty_req = models.CharField(max_length=250, default='n/a', 
                                         verbose_name='CGX Swabs Qty Req', null=True, blank=True)
    cgx_swabs_qty_auth = models.CharField(max_length=250, default='n/a',
                                         verbose_name='CGX Swabs Qty Auth', null=True, blank=True)
    cgx_req_forms_qty_req = models.CharField(max_length=250, default='n/a', 
                                              verbose_name='CGX Req. Forms Qty Req.', null=True, blank=True)
    cgx_req_forms_qty_auth = models.CharField(max_length=250, default='n/a',
                                             verbose_name='CGX Req. Forms Qty Auth.', null=True, blank=True)
    tubes_tiger_qty_req = models.CharField(max_length=250, default='n/a', 
                                              verbose_name='Tubes Tiger Qty Req.', null=True, blank=True)
    tubes_tiger_qty_auth = models.CharField(max_length=250, default='n/a', 
                                              verbose_name='Tubes Tiger Qty Auth.', null=True, blank=True)
    tubes_lavender_qty_req = models.CharField(max_length=250, default='n/a', 
                                              verbose_name='Tubes Lavender Qty Req.', null=True, blank=True)
    tubes_lavender_qty_auth = models.CharField(max_length=250, default='n/a', 
                                              verbose_name='Tubes Lavender Qty Auth.', null=True, blank=True)
    tubes_red_top_qty_req = models.CharField(max_length=250, default='n/a',
                                               verbose_name='Tubes Red Top Qty Req.', null=True, blank=True)
    tubes_red_top_qty_auth = models.CharField(max_length=250, default='n/a',
                                             verbose_name='Tubes Red Top Qty Auth.', null=True, blank=True)
    tubes_blue_qty_req = models.CharField(max_length=250, default='n/a',
                                             verbose_name='Tubes Blue Qty Req.', null=True, blank=True)
    tubes_blue_qty_auth = models.CharField(max_length=250, default='n/a',
                                          verbose_name='Tubes Blue Qty Auth.', null=True, blank=True)
    tubes_dark_blue_qty_req = models.CharField(max_length=250, default='n/a',
                                          verbose_name='Tubes Dark Blue Qty Req.', null=True, blank=True)
    tubes_dark_blue_qty_auth = models.CharField(max_length=250, default='n/a',
                                          verbose_name='Tubes Dark Blue Qty Auth.', null=True, blank=True)
    tubes_violet_qty_req = models.CharField(max_length=250, default='n/a',
                                          verbose_name='Tubes Violet Qty Req.', null=True, blank=True)
    tubes_violet_qty_auth = models.CharField(max_length=250, default='n/a',
                                          verbose_name='Tubes Violet Qty Auth.', null=True, blank=True)
    straight_needle_18_qty_req = models.CharField(max_length=250, default='n/a',
                                                verbose_name='Straight Needle(18 Gauge) Qty Req',
                                                null=True, blank=True)
    straight_needle_18_qty_auth = models.CharField(max_length=250, default='n/a',
                                                  verbose_name='Straight Needle(18 Gauge) Qty Auth',
                                                  null=True, blank=True)
    straight_needle_20_qty_req = models.CharField(max_length=250, default='n/a',
                                                  verbose_name='Straight Needle(20 Gauge) Qty Req',
                                                  null=True, blank=True)
    straight_needle_20_qty_auth = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Straight Needle(20 Gauge) Qty Auth',
                                                   null=True, blank=True)
    straight_needle_21_qty_req = models.CharField(max_length=250, default='n/a',
                                                  verbose_name='Straight Needle(21 Gauge) Qty Req',
                                                  null=True, blank=True)
    straight_needle_21_qty_auth = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Straight Needle(21 Gauge) Qty Auth',
                                                   null=True, blank=True)
    straight_needle_22_qty_req = models.CharField(max_length=250, default='n/a',
                                                  verbose_name='Straight Needle(22 Gauge) Qty Req',
                                                  null=True, blank=True)
    straight_needle_22_qty_auth = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Straight Needle(22 Gauge) Qty Auth',
                                                   null=True, blank=True)
    straight_needle_23_qty_req = models.CharField(max_length=250, default='n/a',
                                                  verbose_name='Straight Needle(23 Gauge) Qty Req',
                                                  null=True, blank=True)
    straight_needle_23_qty_auth = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Straight Needle(23 Gauge) Qty Auth',
                                                   null=True, blank=True)
    butterfly_needle_18_qty_req = models.CharField(max_length=250, default='n/a',
                                                  verbose_name='Butterfly Needle(18 Gauge) Qty Req',
                                                  null=True, blank=True)
    butterfly_needle_18_qty_auth = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Butterfly Needle(18 Gauge) Qty Auth',
                                                   null=True, blank=True)
    butterfly_needle_20_qty_req = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Butterfly Needle(20 Gauge) Qty Req',
                                                   null=True, blank=True)
    butterfly_needle_20_qty_auth = models.CharField(max_length=250, default='n/a',
                                                    verbose_name='Butterfly Needle(20 Gauge) Qty Auth',
                                                    null=True, blank=True)
    butterfly_needle_21_qty_req = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Butterfly Needle(21 Gauge) Qty Req',
                                                   null=True, blank=True)
    butterfly_needle_21_qty_auth = models.CharField(max_length=250, default='n/a',
                                                    verbose_name='Butterfly Needle(21 Gauge) Qty Auth',
                                                    null=True, blank=True)
    butterfly_needle_22_qty_req = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Butterfly Needle(22 Gauge) Qty Req',
                                                   null=True, blank=True)
    butterfly_needle_22_qty_auth = models.CharField(max_length=250, default='n/a',
                                                    verbose_name='Butterfly Needle(22 Gauge) Qty Auth',
                                                    null=True, blank=True)
    butterfly_needle_23_qty_req = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Butterfly Needle(23 Gauge) Qty Req',
                                                   null=True, blank=True)
    butterfly_needle_23_qty_auth = models.CharField(max_length=250, default='n/a',
                                                    verbose_name='Butterfly Needle(23 Gauge) Qty Auth',
                                                    null=True, blank=True)
    needle_vacuum_tubes_18_qty_req = models.CharField(max_length=250, default='n/a',
                                                   verbose_name='Need Vacuum Tubes Qty Req',
                                                   null=True, blank=True)
    needle_vacuum_tubes_18_qty_auth = models.CharField(max_length=250, default='n/a',
                                                    verbose_name='Need Vacuum Tubes Qty Auth',
                                                    null=True, blank=True)
    uti_cups_qty_req = models.CharField(max_length=250, default='n/a',
                                    verbose_name='UTI Cups Qty Req.', null=True, blank=True)
    uti_cups_qty_auth = models.CharField(max_length=250, default='n/a',
                                        verbose_name='UTI Cups Qty Auth.', null=True, blank=True)
    uti_urine_tubes_qty_req = models.CharField(max_length=250, default='n/a',
                                        verbose_name='UTI Urine Tubes Qty Req.', null=True, blank=True)
    uti_urine_tubes_qty_auth = models.CharField(max_length=250, default='n/a',
                                               verbose_name='UTI Urine Tubes Qty Auth.', null=True, blank=True)
    culture_swabs_qty_req = models.CharField(max_length=250, default='n/a',
                                            verbose_name='Culture Swabs Qty Req', null=True, blank=True)
    culture_swabs_qty_auth = models.CharField(max_length=250, default='n/a',
                                             verbose_name='Culture Swabs Qty Auth', null=True, blank=True)
    tourniquets_qty_req = models.CharField(max_length=250, default='n/a',
                                            verbose_name='Tourniquets Qty Req', null=True, blank=True)
    tourniquets_qty_auth = models.CharField(max_length=250, default='n/a',
                                           verbose_name='Tourniquets Qty Auth', null=True, blank=True)
    gauze_qty_req = models.CharField(max_length=250, default='n/a',
                                    verbose_name='Gauze Qty Req', null=True, blank=True)
    gauze_qty_auth = models.CharField(max_length=250, default='n/a',
                                    verbose_name='Gauze Qty Auth', null=True, blank=True)
    bandages_qty_req = models.CharField(max_length=250, default='n/a',
                                    verbose_name='Bandages Qty Req', null=True, blank=True)
    bandages_qty_auth = models.CharField(max_length=250, default='n/a',
                                    verbose_name='Bandages Qty Auth', null=True, blank=True)
    gel_pack_qty_req = models.CharField(max_length=250, default='n/a',
                                    verbose_name='Gel Pack Qty Req', null=True, blank=True)
    gel_pack_qty_auth = models.CharField(max_length=250, default='n/a',
                                    verbose_name='Gel Pack Qty Auth', null=True, blank=True)

    class Meta:
        verbose_name = 'Supply'
        verbose_name_plural = 'Supplies'
        ordering=['sale_rep_name']

    def __str__(self):
        return self.sale_rep_name
