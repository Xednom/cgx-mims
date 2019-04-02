import django_filters
from django_filters import DateRangeFilter, DateFilter, CharFilter

from rest_framework import viewsets, filters
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from django.views.generic import TemplateView


from cgx.models import Agent, Manager
from .models import Carrier
from cgx.serializers import AgentSerializer, ManagerSerializer
from .serializers import CarrierSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class CarrierSearchFilter(django_filters.FilterSet):
    patient_name = CharFilter(field_name='patient_name', lookup_expr='patient_name')

    class Meta:
        model = Carrier
        fields = ('patient_name',)


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
    serializer_class = CarrierSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    #  renderer_classes = (XLSXRenderer,) # commented this to be able to view the ModelViewSet in the API
    parser_classes = (MultiPartParser,) #  for uploading of attachments
    filename = 'carrier-reports.xlsx'
    filter_class = (CarrierFilter) #  filtering From date and To date
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

    def perform_create(self, serializer):
        user = self.request.user
        promo_code = self.request.user.agent_promo_code
        serializer.save(created_by=user, user_promo_code=promo_code)
