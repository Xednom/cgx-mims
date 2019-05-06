from django.urls import path
from . import views

app_name='carrier'

urlpatterns = [
    path('view-carrier', views.CarrierView.as_view(), name="view-carrier"),
    path('add-carrier', views.AddCarrierView.as_view(), name="add-carrier"),
    path('<uuid:carrier_id>/carrier-report.pdf', views.PdfCarrier.as_view(), name="print_carrier"),
    path('carrier-report.xlsx', views.ExcelCarrier.as_view(), name="excel_carrier"),
]
