from django.urls import path
from . import views

app_name = 'dme'
urlpatterns = [
    path('view-dme', views.DmeView.as_view(), name='view-dme'),
    path('add-dme', views.AddDmeView.as_view(), name='add-dme')
]