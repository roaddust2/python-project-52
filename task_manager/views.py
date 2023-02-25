from django.shortcuts import render
from django.views.generic import (
    TemplateView,
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

class MainPageView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    template_name='login.html'
    next_page = 'index'


class CustomLogoutView(LogoutView):
    next_page = 'index'
