from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

from django.shortcuts import render
from django.views.generic import TemplateView
from tablib import Dataset
import openpyxl, datetime

from .resources import BioConfirmMasterResource
from .models import Agent, BioConfirmMaster, Manager
from .serializers import AgentSerializer, BioConfirmMasterSerializer, ManagerSerializer

from .models import Agent, Manager, BioConfirmMaster
from .serializers import (AgentSerializer, ManagerSerializer,
                          BioConfirmMasterSerializer)


class CsrftExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # will not enforce a csrf check


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class BioConfirmMasterViewSet(viewsets.ModelViewSet):
    # queryset = BioConfirmMaster.objects.all()
    serializer_class = BioConfirmMasterSerializer
    authentication_classes = (CsrftExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    filter_backends = [filters.SearchFilter]
    search_fields = ('promo_code', 'patient_name')

    def get_queryset(self):
        user = self.request.user
        queryset = BioConfirmMaster.objects.filter(agent__name=user)
        return queryset


class BioConfirmView(TemplateView):
    template_name = 'cgx/bioconfirm.html'


def index(request):
    if request.method == "POST":
        bioconfirm_resource = BioConfirmMasterResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read())
        result = bioconfirm_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            bioconfirm_resource.import_data(dataset, dry_run=True)

    return render(request, 'cgx/index.html')


def upload_bcm(request):
    if "GET" == request.method:
        return render(request, 'cgx/upload_bcm.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb.active
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        save_bcm(excel_data)

        return render(request, 'cgx/upload_bcm.html', {})


def save_bcm(excel_data):
    for row in excel_data[1:]:
        print("\n\nRow: ", row)
        print("\n\n")
        new_bcm = BioConfirmMaster(
            patient_name=row[0],
            patient_phone_number=row[1],
            promo_code=row[2],
            agent=add_agents(row[3]),
            date_app_rec=set_date(row[5]),
            date_sample_rec=set_date(row[6]),
            type_of_test=blank_inputs(row[7]),
            date_of_qca=set_date(row[8]),
            submitted_to_tamika_ins_verifier=set_date(row[9]),
            telemed_name=row[10],
            date_submitted_to_telemed=set_date(row[11]),
            date_telemed_returned=set_date(row[12]),
            date_bioconfim_rec_app=set_date(row[13]),
            date_paid=set_date(row[15]),
            state=row[16],
            status=row[17],
            month=row[18],
            insurance_company=row[19],
            notes=row[20],
            rejection_date=set_date(row[21]),
        )

        print("New BCM: ", new_bcm)
        print("\n\n")

        new_bcm.save()


def add_managers(manager):

    if not Manager.objects.filter(name=manager):
        print("Row:", manager)
        new_manager = Manager(name=manager)
        new_manager.save()

        return Manager.objects.get(name=new_manager.name)


def add_agents(agent):
    print("\nAgent: ", agent)

    if not Agent.objects.filter(name=agent):
        print("Row:", agent)
        new_agent = Agent(name=agent)
        new_agent.save()

        return Agent.objects.get(name=new_agent.name)

    return Agent.objects.get(name=agent.name)


def set_date(date):
    print("Original date: ", date)
    print("Type: ", type(date))
    if date != 'None' or date.strip() != "":
        print("Hello")

        print("Date: ", date.split("-"))
        split_date = date.split("-")
        print("Day: ", split_date[2][:2])
        print("\n\n")
        date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2][:2]))
        print("New Date: ", date)
        print("\n\n")

        return date

    return None


def blank_inputs(input):
    if input == 'None':
        return None
    return input
