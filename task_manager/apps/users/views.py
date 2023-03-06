from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from task_manager.utils.text import Titles, Messages


title = Titles()
message = Messages()


class UsersListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'crud/list.html'

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['users_list'] = True
        context['list_title'] = title.users_read
        return context


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'crud/create.html'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['create_title'] = title.user_create
        return context

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            message.user_create_succ,
            extra_tags='success'
        )
        return reverse('login')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'crud/update.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['update_title'] = title.user_update
        return context

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def handle_no_permission(self):
        messages.add_message(
            self.request,
            messages.ERROR,
            message.user_update_err,
            extra_tags='danger'
        )
        return redirect('users_index')

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            message.user_update_succ,
            extra_tags='success'
        )
        return reverse('users_index')


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'crud/delete.html'

    def get_context_data(self, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['delete_title'] = title.user_delete
        return context

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def handle_no_permission(self):
        messages.add_message(
            self.request,
            messages.ERROR,
            message.user_delete_err,
            extra_tags='danger'
        )
        return redirect('users_index')

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            message.user_delete_succ,
            extra_tags='danger'
        )
        return reverse('users_index')
