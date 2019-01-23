from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('add', views.AddRecordView.as_view(), name='add_record')

]
