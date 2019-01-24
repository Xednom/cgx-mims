from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Carrier
from .serializers import CarrierSerializer


class CarrierViewSet(viewsets.ModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('patient_name', 'promo_code')
