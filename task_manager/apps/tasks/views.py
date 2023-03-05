from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from task_manager.apps.tasks.models import Task
from task_manager.apps.tasks.forms import CustomTaskCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'crud/list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)
        context['list_title'] = _('TasksListTitle')
        context['create_button'] = {"url": 'tasks_create', "name": _('TasksListButtonName')}
        context['tasks_list'] = True
        return context


class TaskDetaileView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task.html'


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CustomTaskCreationForm
    template_name = 'crud/create.html'
    success_message = _('TaskCreateAlertSuccess')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks_index')


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = CustomTaskCreationForm
    template_name = 'crud/update.html'
    success_message = _('TaskUpdateAlertSuccess')

    def get_success_url(self):
        return reverse('tasks_index')


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'crud/delete.html'
    success_message = _('TaskDeleteAlertSuccess')

    def get_success_url(self):
        return reverse('tasks_index')
