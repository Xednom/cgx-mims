from django.shortcuts import render
from tablib import Dataset
import openpyxl, uuid

from .resources import BioConfirmMasterResource
from .models import Agent, BioConfirmMaster, Manager
from .serializers import AgentSerializer, BioConfirmMasterSerializer, ManagerSerializer


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
        return render(request, 'cgx/upload.html', {})
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
        print(excel_data[0])

        return render(request, 'cgx/upload.html', {"excel_data": excel_data})


def upload_managers(request):
    if "GET" == request.method:
        return render(request, 'cgx/upload_managers.html', {})
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
        print(excel_data[0])

        for row in excel_data[1:]:
            if not Manager.objects.filter(name=row[0]):
                print("Row:", row[0])
                manager = Manager(name=row[0])
                print("Manager: ", manager)
                serializer = ManagerSerializer(data=manager)
                print("Data:", serializer.is_valid())
                print("\n\n\n")

                serializer.save()

        return render(request, 'cgx/upload_managers.html', {"excel_data": excel_data})


def upload_agents(request):
    if "GET" == request.method:
        return render(request, 'cgx/upload_agents.html', {})
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
        print(excel_data[0])

        return render(request, 'cgx/upload_agents.html', {"excel_data": excel_data})

