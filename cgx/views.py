from django.shortcuts import render
import openpyxl


def cgx_excel(request):
    if request.method == "GET":
        return render(request, 'cgx/excel_upload.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        print("\n\nExcel File: ", excel_file.name)
        excel_file = excel_file.name
        print("excel file type: ", type(excel_file))
        print("\n")
        wb = openpyxl.load_workbook(excel_file)
        print("WB: ", wb)
        print("\n")
        worksheet = wb["BIO CONFIRM MASTER"]
        print("worksheet: ", worksheet)
        print("\n")

        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        print("Excel data: ", excel_data)
        print("\n")

        return render(request, 'cgx/excel_upload.html', {"excel_data" : excel_data})
