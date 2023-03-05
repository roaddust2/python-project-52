from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
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
from task_manager.apps.users.forms import CustomUserCreationForm
from django.contrib.auth.models import User


class UsersListView(ListView):
    model = User
    template_name = 'crud/list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['list_title'] = _('UsersListTitle')
        context['users_list'] = True
        return context


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'crud/create.html'

    def get_success_url(self):
        return reverse('login')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'crud/update.html'

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
    template_name = 'crud/delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def handle_no_permission(self):
        messages.add_message(self.request, messages.ERROR, _('UsersUpdateError'), extra_tags='danger')
        return redirect('users_index')

    def get_success_url(self):
        return reverse('users_index')
