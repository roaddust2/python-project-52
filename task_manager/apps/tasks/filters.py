from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django.contrib.auth.models import User
from task_manager.apps.tags.models import Tag
from task_manager.apps.tasks.models import Task
from task_manager.apps.statuses.models import Status
from django import forms
from task_manager.utils.text import FormFields


field = FormFields()


class TasksFilterSet(FilterSet):

    def self_tasks_filter(self, queryset, name, value):
        if value:
            author = getattr(self.request, 'user')
            queryset = queryset.filter(author=author)
        return queryset

    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=field.tasks_filter_status,
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
        label=field.tasks_filter_performer,
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
        label=field.tasks_filter_tags,
        widget=forms.Select(
            attrs={
                'name': 'tags',
                'class': 'form-control',
                'title_id': 'id_tags'
            }
        )
    )

    self_tasks = BooleanFilter(
        label=field.tasks_filter_self_tasks,
        widget=forms.widgets.CheckboxInput(
            attrs={
                'name': 'self_task',
                'title_id': 'id_self_task'
            }
        ),
        method='self_tasks_filter',
    )

    class Meta:
        model = Task
        fields = ['status', 'performer', 'tags']
