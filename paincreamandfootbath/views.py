from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer

from django.shortcuts import render

from .models import PainCreamAndFootBath

from .serializers import PainCreamAndFootBathSerializer


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class PainCreamAndFootBathViewSet(XLSXFileMixin, viewsets.ModelViewSet):
    serializer_class = PainCreamAndFootBathSerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
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
