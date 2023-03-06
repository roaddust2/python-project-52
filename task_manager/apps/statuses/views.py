from task_manager.apps.statuses.models import Status
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import StatusForm
from django.urls import reverse
from task_manager.utils.text import Titles, Messages, Buttons


title = Titles()
message = Messages()
button = Buttons()


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'crud/list.html'
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super(StatusesListView, self).get_context_data(**kwargs)
        context['statuses_list'] = True
        context['list_title'] = title.statuses_list
        context['create_button'] = {
            "url": 'statuses_create',
            "name": button.statuses_create_btn
        }
        return context


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = 'crud/create.html'
    success_message = message.status_create_succ

    def get_context_data(self, **kwargs):
        context = super(StatusCreateView, self).get_context_data(**kwargs)
        context['create_title'] = title.status_create
        return context

    def get_success_url(self):
        return reverse('statuses_index')


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'crud/update.html'
    success_message = message.status_update_succ

    def get_context_data(self, **kwargs):
        context = super(StatusUpdateView, self).get_context_data(**kwargs)
        context['update_title'] = title.status_update
        return context

    def get_success_url(self):
        return reverse('statuses_index')


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'crud/delete.html'
    success_message = message.status_delete_succ

    def get_success_url(self):
        return reverse('statuses_index')
