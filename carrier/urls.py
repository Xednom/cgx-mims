from django.urls import path
from . import views

app_name='carrier'

urlpatterns = [
    path('carrier-report/', views.PDFView.as_view(), name="print_carrier")
]