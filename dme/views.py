import django_filters
from django_filters import DateRangeFilter, DateFilter, CharFilter

from rest_framework import viewsets, filters
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import DME_II
from .serializers import DMEIISerializer


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class DmeView(LoginRequiredMixin, TemplateView):
    template_name = 'dme/dme.html'
    

class AddDmeView(LoginRequiredMixin, TemplateView):
    template_name = 'dme/add_patient_dme.html'

class DMEFilter(django_filters.FilterSet):
    submission_date__gte = DateFilter(field_name='submission_date', lookup_expr='gte')
    submission_date__lte = DateFilter(field_name='submission_date', lookup_expr='lte')
    patients_first_name = CharFilter(field_name='patients_first_name', lookup_expr='icontains')
    patients_last_name = CharFilter(field_name='patients_last_name', lookup_expr='icontains')

    class Meta:
        model = DME_II
        fields = ('submission_date__gte', 'submission_date__lte', 
                  'patients_first_name', 'patients_last_name')


class DMEIIViewSet(XLSXFileMixin, viewsets.ModelViewSet):
    # queryset = DME_II.objects.all()
    serializer_class = DMEIISerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    filter_class = (DMEFilter)
    search_fields = ('first_name', 'last_name', 'agents_promod_code')
    filename = 'dme-reports.xlsx'

    def get_queryset(self):
        agent_promo_code = self.request.user.agent_promo_code
        return DME_II.objects.filter(agents_promod_code=agent_promo_code)
    
    def perform_create(self, serializer):
        user = self.request.user
        promo_code = self.request.user.agent_promo_code
        serializer.save(created_by=user, user_promo_code=promo_code)
