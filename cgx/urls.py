"""cgx_mims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'cgx'

urlpatterns = [
    path('view-bioconfirm', views.BioConfirmView.as_view(), name='bioconfirm'),
    path('add-bioconfirm', views.AddBioConfirmView.as_view(), name='add-bioconfirm'),
    path('cgx_upload_data/', views.upload_bcm, name='upload_bcm'),
    path('<uuid:bioconfirm_id>/bioconfirm-report.pdf', views.PdfBioconfirm.as_view(), name='bioconfirm_print'),
]
