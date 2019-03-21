import django_filters
from django_filters import DateRangeFilter, DateFilter, CharFilter

from rest_framework import viewsets, filters
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_pandas import PandasView, PandasCSVRenderer, PandasExcelRenderer

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import DME_II
from .serializers import DMEIISerializer


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class DMEFilter(django_filters.FilterSet):
    submission_date__gte = DateFilter(field_name='submission_date', lookup_expr='gte')
    submission_date__lte = DateFilter(field_name='submission_date', lookup_expr='lte')
    patients_first_name = CharFilter(field_name='patients_first_name', lookup_expr='icontains')
    patients_last_name = CharFilter(field_name='patients_last_name', lookup_expr='icontains')

    class Meta:
        model = DME_II
        fields = ('submission_date__gte', 'submission_date__lte', 
                  'patients_first_name', 'patients_last_name')


class DMEIIViewSet(viewsets.ModelViewSet):
    # queryset = DME_II.objects.all()
    serializer_class = DMEIISerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    filter_class = (DMEFilter)
    search_fields = ('first_name', 'last_name', 'agents_promod_code')

    def get_queryset(self):
        agent_promo_code = self.request.user.agent_promo_code
        return DME_II.objects.filter(agents_promod_code=agent_promo_code)

    def post(self, request, format=None):
        #  to access files
        print (request.FILES)
        #  to access data
        print (request.data)
        return Response({'recieved data': request.data})


class DMEExcelExtract(PandasView):
    queryset = DME_II.objects.all()
    serializer_class = DMEIISerializer
    renderer_classes = [PandasCSVRenderer, PandasExcelRenderer]

    def filter_queryset(self):
        agent_promo_code = self.request.user.agent_promo_code
        return DME_II.objects.filter(agents_promod_code=agent_promo_code)