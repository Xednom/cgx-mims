import django_filters
from django_filters import DateFilter, CharFilter

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.views.generic import TemplateView

from cgx.models import Agent, Manager
from .models import Insurance, TypeOfInsurance

from cgx.serializers import AgentSerializer, ManagerSerializer
from .serializers import InsuranceSerializer, TypeOfInsuranceSerializer


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AgentSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ManagerSerializer


class TypeOfInsuranceViewSet(viewsets.ModelViewSet):
    queryset = TypeOfInsurance.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TypeOfInsuranceSerializer


class InsuranceFilter(django_filters.FilterSet):
    date_created__gte = DateFilter(field_name='date_created', lookup_expr='gte')
    date_created__lte = DateFilter(field_name='date_created', lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    promo_code = CharFilter(field_name='promo_code', lookup_expr='icontains')

    class Meta:
        model = Insurance
        fields = ('date_created__gte', 'date_created__lte',
                  'name', 'promo_code',)


class InsuranceViewSet(viewsets.ModelViewSet):
    # queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_class = (InsuranceFilter)
    search_fields = ('name', 'promo_code')

    def get_queryset(self):
        user = self.request.user
        queryset = Insurance.objects.filter(agent__name=user)
        return queryset
