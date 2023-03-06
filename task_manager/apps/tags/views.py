from django.db import IntegrityError
from .models import Tag
from task_manager.apps.tasks.models import Task
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from task_manager.apps.tags.forms import TagForm
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from task_manager.utils.text import Titles, Messages, Buttons


title = Titles()
message = Messages()
button = Buttons()


class TagsListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'crud/list.html'
    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super(TagsListView, self).get_context_data(**kwargs)
        context['tags_list'] = True
        context['list_title'] = title.tags_list
        context['create_button'] = {
            "url": 'tags_create',
            "name": button.tag_create_btn
        }
        return context


class TagCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TagForm
    template_name = 'crud/create.html'
    success_message = message.tag_create_succ

    def get_context_data(self, **kwargs):
        context = super(TagCreateView, self).get_context_data(**kwargs)
        context['create_title'] = title.tag_create
        return context

    def get_success_url(self):
        return reverse('tags_index')


class TagUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'crud/update.html'
    success_message = message.tag_update_succ

    def get_context_data(self, **kwargs):
        context = super(TagUpdateView, self).get_context_data(**kwargs)
        context['update_title'] = title.tag_update
        return context

    def get_success_url(self):
        return reverse('tags_index')


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('tags_index')

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            tag = self.get_object()
            if Task.objects.filter(tags=tag).exists():
                raise IntegrityError
            self.object.delete()
            messages.add_message(
                self.request,
                messages.SUCCESS,
                message.tag_delete_succ,
                extra_tags='success'
            )
        except IntegrityError:
            messages.add_message(
                self.request,
                messages.SUCCESS,
                message.tag_delete_err,
                extra_tags='danger'
            )
        finally:
            return redirect(success_url)
