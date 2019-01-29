from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import DME_II
from .serializers import DMEIISerializer


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class DMEIIViewSet(viewsets.ModelViewSet):
    queryset = DME_II.objects.all()
    serializer_class = DMEIISerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    filter_backends = [filters.SearchFilter]
    search_fields = ('first_name', 'last_name', 'agents_promod_code')
