import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.http import JsonResponse

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin

from carrier.models import Carrier
from django.db.models import Count


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class LoginView(AuthenticationForm, View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('web:home'))
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and password is not None:
            login(request, user)
            user.last_login = datetime.datetime.now()
            user.save(update_fields=['last_login'])
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect(reverse_lazy('web:home'))
        else:
            messages.warning(request, 'Incorrect username or password')
        return render(request, self.template_name)


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Your account has been logout successfully')
        return redirect(reverse_lazy('web:login'))


class AddRecordView(LoginRequiredMixin, TemplateView):
    template_name = 'add_records_all_apps.html'
