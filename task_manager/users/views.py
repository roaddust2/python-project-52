from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from task_manager.users.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Create your views here.
class UsersListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class UsersCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'

    def get_success_url(self):
        return reverse('login')


class UsersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/update.html'

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def handle_no_permission(self):
        messages.add_message(self.request, messages.ERROR, _('UsersUpdateError'), extra_tags='danger')
        return redirect('users_index')

    def get_success_url(self):
        return reverse('users_index')


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user
    
    def handle_no_permission(self):
        messages.add_message(self.request, messages.ERROR, _('UsersUpdateError'), extra_tags='danger')
        return redirect('users_index')

    def get_success_url(self):
        return reverse('users_index')
