from django.urls import path

from . import views

app_name = 'supplies'
urlpatterns = [
    path('request-supplies/', views.AddSupplyView.as_view(), name='add_supplies')
]
