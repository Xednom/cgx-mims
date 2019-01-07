from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication

from .models import Agent, Manager, BioConfirmMaster
from .serializers import (AgentSerializer, ManagerSerializer,
                          BioConfirmMasterSerializer)


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class BioConfirmMasterViewSet(viewsets.ModelViewSet):
    queryset = BioConfirmMaster.objects.all()
    serializer_class = BioConfirmMasterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('promo_code', 'patient_name')
