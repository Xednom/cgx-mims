from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Insurance
from .serializers import InsuranceSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'promo_code')
