from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.apps.statuses.models import Status
from task_manager.apps.statuses.forms import StatusForm


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = 'crud/create.html'
    success_message = _('StatusCreateAlertSuccess')
    
    def get_success_url(self):
        return reverse('statuses_index')


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'crud/update.html'
    success_message = _('StatusUpdateAlertSuccess')
    
    def get_success_url(self):
        return reverse('statuses_index')


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'crud/delete.html'
    success_message = _('StatusDeleteAlertSuccess')

    def get_success_url(self):
        return reverse('statuses_index')