from django.urls import path
from . import views

app_name='carrier'

urlpatterns = [
    path('carrier-report.pdf', views.PdfCarrier.as_view(), name="print_carrier")
]
