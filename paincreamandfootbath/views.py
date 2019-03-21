from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_pandas import PandasView, PandasCSVRenderer, PandasExcelRenderer

from django.shortcuts import render

from .models import PainCreamAndFootBath

from .serializers import PainCreamAndFootBathSerializer


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class PainCreamAndFootBathViewSet(viewsets.ModelViewSet):
    serializer_class = PainCreamAndFootBathSerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ('patient_first_name', 'patient_last_name', 'promo_code',)

    def get_queryset(self):
        user = self.request.user
        queryset = PainCreamAndFootBath.objects.filter(agent_name__name=user)
        return queryset


class ExcelExtract(PandasView):
    queryset = PainCreamAndFootBath.objects.all()
    serializer_class = PainCreamAndFootBathSerializer
    renderer_classes = [PandasCSVRenderer, PandasExcelRenderer]

    def filter_queryset(self):
        user = self.request.user
        qs = PainCreamAndFootBath.objects.filter(agent__name=user)
        return qs