from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import render
from tablib import Dataset
import openpyxl, uuid

from .resources import BioConfirmMasterResource
from .models import Agent, BioConfirmMaster, Manager
from .serializers import AgentSerializer, BioConfirmMasterSerializer, ManagerSerializer

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
    for row in excel_data:
        new_bcm = BioConfirmMaster(
            patient_name=row[0],
            patient_phone_number=row[1],
            promo_code=row[2],
            agent=add_agents(name=row[3]),
            date_app_rec=row[5],
            date_sample_rec=row[6],
            type_of_test =row[7],
            date_of_qca=row[8],
            submitted_to_tamika_ins_verifier=row[9],
            telemed_name=row[10],
            date_submitted_to_telemed=row[11],
            date_telemed_returned=row[12],
            date_bioconfim_rec_app=row[13],
            date_paid=row[15],
            state=row[16],
            status=row[17],
            month=row[18],
            insurance_company=row[19],
            notes=row[20],
            rejection_date=row[21],
        )

        new_bcm.save()


def add_managers(manager):

    if not Manager.objects.filter(name=manager):
        print("Row:", manager)
        new_manager = Manager(name=manager)
        new_manager.save()

        return new_manager


def add_agents(agent):

    if not Agent.objects.filter(name=agent):
        print("Row:", agent)
        new_agent = Manager(name=agent)
        new_agent.save()

        return Agent.objects.get(name=new_agent.name)
