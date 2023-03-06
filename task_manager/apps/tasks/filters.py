from django_filters import FilterSet, ModelChoiceFilter
from django.contrib.auth.models import User
from task_manager.apps.tags.models import Tag
from task_manager.apps.tasks.models import Task
from task_manager.apps.statuses.models import Status
from django.utils.translation import gettext_lazy as _
from django import forms


class TasksFilterSet(FilterSet):
    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('TasksFilterStatusLabel'),
        widget=forms.Select(
            attrs={
                'name': 'status',
                'class': 'form-control',
                'title_id': 'id_status'
            }
        )
    )

    performer = ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('TasksFilterPerformerLabel'),
        widget=forms.Select(
            attrs={
                'name': 'performer',
                'class': 'form-control',
                'title_id': 'id_performer'
            }
        )
    )

    tags = ModelChoiceFilter(
        queryset=Tag.objects.all(),
        label=_('TasksFilterTagsLabel'),
        widget=forms.Select(
            attrs={
                'name': 'tags',
                'class': 'form-control',
                'title_id': 'id_tags'
            }
        )
    )
    
    class Meta:
        model = Task
        fields = ['status', 'performer', 'tags']
