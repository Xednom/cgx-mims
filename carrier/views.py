from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

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


class CarrierViewSet(viewsets.ModelViewSet):
    # queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    filter_backends = [filters.SearchFilter]
    search_fields = ('patient_name', 'promo_code')

    def get_queryset(self):
        user = self.request.user
        queryset = Carrier.objects.filter(agent__name=user)
        return queryset
