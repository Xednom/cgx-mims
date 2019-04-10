from django.urls import path

from . import views

app_name = 'pcfb'
urlpatterns = [
    path('view-rx', views.PcFbView.as_view(), name="view-pcandfb"),
    path('add-rx', views.AddPcFbView.as_view(), name="add-pcandfb")
]
