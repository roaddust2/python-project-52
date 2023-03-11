from .models import Task
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django_filters.views import FilterView
from .filters import TasksFilterSet
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from task_manager.utils.text import Titles, Messages, Buttons


title = Titles()
message = Messages()
button = Buttons()


class TasksListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'crud/list.html'
    context_object_name = 'tasks'
    filterset_class = TasksFilterSet

    def get_context_data(self, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)
        context['tasks_list'] = True
        context['list_title'] = title.tasks_list
        context['create_button'] = {
            "url": 'tasks_create',
            "name": button.task_create_btn
        }
        return context


class TaskDetaileView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task.html'


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'performer', 'tags']
    template_name = 'crud/create.html'
    success_message = message.task_create_succ

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['create_title'] = title.task_create
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks_index')


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'performer', 'tags']
    template_name = 'crud/update.html'
    success_message = message.task_update_succ

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['update_title'] = title.task_update
        return context

    def get_success_url(self):
        return reverse('tasks_index')


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'crud/delete.html'
    success_message = message.task_delete_succ

    def get_context_data(self, **kwargs):
        context = super(TaskDeleteView, self).get_context_data(**kwargs)
        context['delete_title'] = title.task_delete
        return context

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def handle_no_permission(self):
        messages.add_message(
            self.request,
            messages.ERROR,
            message.task_delete_err,
            extra_tags='danger'
        )
        return redirect('tasks_index')

    def get_success_url(self):
        return reverse('tasks_index')
