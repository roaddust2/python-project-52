from django.db import IntegrityError
from .models import Label
from task_manager.apps.tasks.models import Task
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from task_manager.utils.text import Titles, Messages, Buttons


title = Titles()
message = Messages()
button = Buttons()


class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'crud/list.html'
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        context = super(LabelsListView, self).get_context_data(**kwargs)
        context['labels_list'] = True
        context['list_title'] = title.labels_list
        context['create_button'] = {
            "url": 'labels_create',
            "name": button.label_create_btn
        }
        return context


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name', 'color']
    template_name = 'crud/create.html'
    success_message = message.label_create_succ

    def get_context_data(self, **kwargs):
        context = super(LabelCreateView, self).get_context_data(**kwargs)
        context['create_title'] = title.label_create
        return context

    def get_success_url(self):
        return reverse('labels_index')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name', 'color']
    template_name = 'crud/update.html'
    success_message = message.label_update_succ

    def get_context_data(self, **kwargs):
        context = super(LabelUpdateView, self).get_context_data(**kwargs)
        context['update_title'] = title.label_update
        return context

    def get_success_url(self):
        return reverse('labels_index')


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('labels_index')

    def get_context_data(self, **kwargs):
        context = super(LabelDeleteView, self).get_context_data(**kwargs)
        context['delete_title'] = title.label_delete
        return context

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            label = self.get_object()
            if Task.objects.filter(labels=label).exists():
                raise IntegrityError
            self.object.delete()
            messages.add_message(
                self.request,
                messages.SUCCESS,
                message.label_delete_succ,
                extra_tags='success'
            )
        except IntegrityError:
            messages.add_message(
                self.request,
                messages.SUCCESS,
                message.label_delete_err,
                extra_tags='danger'
            )
        finally:
            return redirect(success_url)
