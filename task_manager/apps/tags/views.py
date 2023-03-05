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
from task_manager.apps.tags.models import Tag
from task_manager.apps.tags.forms import TagForm


class TagsListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'crud/list.html'
    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super(TagsListView, self).get_context_data(**kwargs)
        context['list_title'] = _('TagsListTitle')
        context['create_button'] = {"url": 'tags_create', "name": _('TagsListButtonName')}
        context['tags_list'] = True
        return context


class TagsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TagForm
    template_name = 'crud/create.html'
    success_message = _('TagCreateAlertSuccess')

    def get_success_url(self):
        return reverse('tags_index')


class TagsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'crud/update.html'
    success_message = _('TagUpdateAlertSuccess')

    def get_success_url(self):
        return reverse('tags_index')


class TagsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tag
    template_name = 'crud/delete.html'
    success_message = _('TagDeleteAlertSuccess')

    def get_success_url(self):
        return reverse('tags_index')
