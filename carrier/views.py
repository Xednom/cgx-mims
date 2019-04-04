import django_filters
from django_filters import DateRangeFilter, DateFilter, CharFilter
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
from django.template import Context
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View
from django.utils import timezone

from cgx.models import Agent, Manager
from .models import Carrier
from cgx.serializers import AgentSerializer, ManagerSerializer
from .serializers import CarrierSerializer
from .render import Render

# 3rd party app(s)
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin

from django.contrib.auth import get_user_model
User = get_user_model()


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class PDFView(PDFTemplateView):
    template_name = 'carrier/carrier.html'
    download_filename = 'carrier_report.pdf'

    def get_context_data(self, **kwargs):
        return super(PDFView, self).get_context_data(
            pagesize='A4',
            title='Carrier Report!',
            **kwargs
        )


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


class CarrierViewSet(XLSXFileMixin, PDFTemplateResponseMixin, ModelViewSet):
    serializer_class = CarrierSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,) #  for uploading of attachments
    filename = 'carrier-reports.xlsx'
    pdf_filename = 'carrier-report.pdf'
    filter_class = (CarrierFilter)  # filtering From date and To date
    filterset_fields = ('patient_name', 'promo_code')
    search_fields = ('patient_name', 'promo_code', 'insurance_verified_tsg_verification')

    def get_queryset(self):
        user = self.request.user
        position = self.request.user.position
        if position == 'Manager':
            queryset = Carrier.objects.filter(manager__name=user)
        else:
            queryset = Carrier.objects.filter(agent__name=user)
        return queryset
    
    def queryset(self, request, format=None):
        carrier = Carrier.objects.all()
        template_path = 'carrier/carrier_print.html'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="carrier-report.pdf"'

        html = render_to_string(template_path, {'carrier': carrier})
        print(html)

        pisaStatus = pisa.CreatePDF(html, dest=response)

        return response

    def perform_create(self, serializer):
        user = self.request.user
        promo_code = self.request.user.agent_promo_code
        serializer.save(created_by=user, user_promo_code=promo_code)

    #  xhtml2pdf
    def get(self, request):
        user = self.request.user
        position = self.request.user.position
        if position == 'Manager':
            queryset = Carrier.objects.filter(manager__name=user)
        else:
            queryset = Carrier.objects.filter(agent__name=user)
        return queryset
        template_path = 'carrier/carrier_print.html'
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="carrier-report.pdf"'
        # find the template and render it.
        html = render_to_string(template_path, {'queryset': queryset})
        print(html)

        # create a pdf
        pisaStatus = pisa.CreatePDF(html, dest=response)

        # if error then show some funny view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
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
