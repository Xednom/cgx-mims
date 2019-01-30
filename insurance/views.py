from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication

from django.shortcuts import render
from django.views.generic import TemplateView

from cgx.models import Agent, Manager
from .models import Insurance

from cgx.serializers import AgentSerializer, ManagerSerializer
from .serializers import InsuranceSerializer


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    # queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'promo_code')

    def get_queryset(self):
        user = self.request.user
        queryset = Insurance.objects.filter(agent__name=user)
        return queryset
