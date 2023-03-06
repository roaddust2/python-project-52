from .models import Tag
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from task_manager.apps.tags.forms import TagForm
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


class TagDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tag
    template_name = 'crud/delete.html'
    success_message = message.tag_delete_succ

    def get_success_url(self):
        return reverse('tags_index')
