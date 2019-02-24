from rest_framework import viewsets, filters
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import DME_II
from .serializers import DMEIISerializer


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class DMEIIViewSet(viewsets.ModelViewSet):
    # queryset = DME_II.objects.all()
    serializer_class = DMEIISerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    filter_backends = [filters.SearchFilter]
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
