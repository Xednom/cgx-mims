import django_filters
from django_filters import DateFilter, CharFilter

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PainCreamAndFootBath

from .serializers import PainCreamAndFootBathSerializer


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class PcFbView(LoginRequiredMixin, TemplateView):
    template_name = 'paincreamandfootbath/pc_and_fb.html'


class AddPcFbView(LoginRequiredMixin, TemplateView):
    template_name = 'paincreamandfootbath/add_patient_pc_and_fb.html'


class PcAndFbFilter(django_filters.FilterSet):
    date_created__gte = DateFilter(field_name='date_created', lookup_expr='gte')
    date_created__lte = DateFilter(field_name='date_created', lookup_expr='lte')
    date_faxed_to_pharmacy__gte = DateFilter(field_name='date_faxed_to_pharmacy', lookup_expr='gte')
    date_faxed_to_pharmacy__lte = DateFilter(field_name='date_faxed_to_pharmacy', lookup_expr='lte')
    submission_date__gte = DateFilter(field_name='submission_date', lookup_expr='gte')
    submission_date__lte = DateFilter(field_name='submission_date', lookup_expr='lte')
    patient_first_name = CharFilter(field_name='patient_first_name', lookup_expr='icontains')
    patient_last_name = CharFilter(field_name='patient_last_name', lookup_expr='icontains')

    class Meta:
        model = PainCreamAndFootBath
        fields = ('date_created__gte', 'date_created__lte',
            'date_faxed_to_pharmacy__gte', 'date_faxed_to_pharmacy__lte',
            'submission_date__gte', 'submission_date__lte',
            'patient_first_name', 'patient_last_name',)



class PainCreamAndFootBathViewSet(XLSXFileMixin, viewsets.ModelViewSet):
    serializer_class = PainCreamAndFootBathSerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_class = (PcAndFbFilter)
    search_fields = ('patient_first_name', 'patient_last_name', 'promo_code',)
    filename = 'pc-and-fb-reports.xlsx'

    def get_queryset(self):
        user = self.request.user
        queryset = PainCreamAndFootBath.objects.filter(agent_name__name=user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        promo_code = self.request.user.agent_promo_code
        serializer.save(created_by=user, user_promo_code=promo_code)
