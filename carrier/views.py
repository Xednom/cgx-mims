import datetime
import django_filters

from django_filters import DateRangeFilter, DateFilter, CharFilter
from openpyxl import Workbook
from xhtml2pdf import pisa

from rest_framework import viewsets, filters
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from django_filters.rest_framework import DjangoFilterBackend


from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import Context
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, ListView
from django.utils import timezone
from django.db.models import Q

from cgx.models import Agent, Manager
from .models import Carrier
from cgx.serializers import AgentSerializer, ManagerSerializer
from .serializers import CarrierSerializer
from .render import Render, render_to_pdf

# 3rd party app(s)
# from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin

from django.contrib.auth import get_user_model
User = get_user_model()


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


# class PDFView(LoginRequiredMixin, PDFTemplateView):
#     template_name = 'carrier/carrier.html'
#     download_filename = 'carrier_report.pdf'

#     def get_context_data(self, **kwargs):
#         return super(PDFView, self).get_context_data(
#             pagesize='A4',
#             title='Carrier Report!',
#             **kwargs
#         )


class CarrierView(LoginRequiredMixin, TemplateView):
    template_name = 'carrier/carrier.html'


class AddCarrierView(LoginRequiredMixin, TemplateView):
    template_name = 'carrier/add_patient_carrier.html'


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    

class CarrierFilter(django_filters.FilterSet):
    date_app_rec__gte = DateFilter(field_name='date_app_rec', lookup_expr='gte')
    date_app_rec__lte = DateFilter(field_name='date_app_rec', lookup_expr='lte')
    date_sample_rec__gte = DateFilter(field_name='date_sample_rec', lookup_expr='gte')
    date_sample_rec__lte = DateFilter(field_name='date_sample_rec', lookup_expr='lte')
    date_of_qca__gte = DateFilter(field_name='date_of_qca', lookup_expr='gte')
    date_of_qca__lte = DateFilter(field_name='date_of_qca', lookup_expr='lte')
    date_created__gte = DateFilter(field_name='date_created', lookup_expr='gte')
    date_created__lte = DateFilter(field_name='date_created', lookup_expr='lte')
    patient_name = CharFilter(field_name='patient_name', lookup_expr='icontains')

    class Meta:
        model = Carrier
        fields = ('date_app_rec__gte', 'date_app_rec__lte', 
                'date_sample_rec__gte', 'date_sample_rec__lte',
                  'date_of_qca__gte', 'date_of_qca__lte',
                  'date_created__gte', 'date_created__lte',
                  'patient_name',)


class CarrierViewSet(XLSXFileMixin, ModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,) #  for uploading of attachments
    filename = 'carrier-reports.xlsx'
    filter_class = (CarrierFilter)  # filtering From date and To date
    filterset_fields = ('patient_name', 'promo_code')
    search_fields = ('patient_name', 'promo_code', 'insurance_verified_tsg_verification')
    response = HttpResponse(content_type='application/xlsx')
    response['Content-Disposition'] = 'attachment; filename="Carrier-Report.xlsx"'
    

    #  xhtml2pdf
    def get(self, request, queryset, *args, **kwargs):
        pdf = render_to_pdf('carrier_print.html', queryset)
        return HttpResponse(pdf, content_type='application/pdf')

    def get_queryset(self):
        user = self.request.user
        position = self.request.user.position
        if position == 'Manager':
            queryset = Carrier.objects.filter(manager__name=user)
        else:
            queryset = Carrier.objects.filter(agent__name=user)
        return queryset
        
    def perform_create(self, serializer):
        user = self.request.user
        promo_code = self.request.user.agent_promo_code
        serializer.save(created_by=user, user_promo_code=promo_code)

    def generate_pdf(self, request):
        template_path = 'carrier/carrier_print.html'

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Carrier-Report.pdf"'

        html = render_to_string(template_path, {'report': report})
        print(html)

        pisaStatus = pisa.CreatePDF(html, dest=response)

        return response


class PdfCarrier(View):

    def get(self, request):
        user = self.request.user
        carriers = Carrier.objects.filter(agent__name=user)
        today = timezone.now()
        params = {
            'today': today,
            'carriers': carriers,
            'request': request
        }

        return Render.render('carrier/carrier_print.html', params)


class ExcelCarrier(View):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        carriers = Carrier.objects.filter(agent__name=user)

        response = self.generate_excel(request, carriers)
        return response

    def generate_excel(self, request, carriers):
        workbook = Workbook()
        filename = 'carrier-reports.xlsx'

        worksheet = workbook.active

        worksheet.append(self.excel_header())

        for carrier in carriers:
            worksheet.append(self.excel_row(carrier))

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename={file}'\
            .format(file = filename)

        workbook.save(response)

        return response

        # SAMPLE FOR EXCEL CONTENT
        # for y in range(1, 101):
        #     for x in range(1, 101):
        #         worksheet.cell(row=x, column=y, value=x*y)

        # workbook.save('/home/station/workstation/files/workbook1.xlsx')

    def excel_row(self, carrier):
        return (
            carrier.patient_name,
            carrier.patient_phone_number,
            carrier.promo_code,
            str(carrier.agent),
            str(carrier.manager),
            carrier.date_app_rec,
            carrier.date_sample_rec,
            str(carrier.type_of_test),
            carrier.date_of_qca,
            carrier.insurance_verified_tsg_verification,
            carrier.telemed_name,
            carrier.date_submitted_to_telemed,
            carrier.date_telemed_returned,
            carrier.date_bioconfim_rec_app,
            carrier.date_paid,
            carrier.date_lab_recorded_app,
            carrier.lab_type,
            carrier.state,
            str(carrier.status),
            carrier.month,
            carrier.insurance_company,
            carrier.notes,
            carrier.rejection_date,
            str(carrier.patient_id_photo),
            str(carrier.insurance_card_photo_front),
            str(carrier.insurance_card_photo_back),
            str(carrier.additional_insurance_cards),
            str(carrier.consent_recording),
            carrier.date_created,
            carrier.created_by,
            carrier.updated_by,
            carrier.user_promo_code
            )

    def excel_header(self):
        return (
            'Patient Name',
            'Patient Phone Number',
            'Promo Code',
            'Agent',
            'Manager',
            'Date App Record',
            'Date Sample Record',
            'Type of Test',
            'Date of QCA',
            'Insurance Verified TSG Verification',
            'Telemed Name',
            'Date Submitted to Telemed',
            'Date Telemed Returned',
            'Date Bioconfim Record App',
            'Date Paid',
            'Date Lab Recorded App',
            'Lab Type',
            'State',
            'status',
            'Month',
            'Insurance Company',
            'Notes',
            'Rejection Date',
            'Patient ID Photo',
            'Insurance Card Photo Front',
            'Insurance Card Photo Back',
            'Additional Insurance Cards',
            'Consent Recording',
            'Date Created',
            'Created by',
            'Updated by',
            'User Promo Code'
            )
