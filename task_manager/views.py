from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages
from task_manager.utils.text import Messages


message = Messages()


class MainPageView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    next_page = 'index'
    success_message = message.user_login_succ


class CustomLogoutView(LogoutView):

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.INFO,
            message.user_logout_succ,
            extra_tags='info'
        )
        return reverse('index')
