from django.views.generic import (
    TemplateView,
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class MainPageView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    next_page = 'index'
    success_message = _('LoginAlertSuccess')


class CustomLogoutView(LogoutView):
    next_page = 'index'
