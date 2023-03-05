from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.apps.tasks.models import Task


class CustomTaskCreationForm(forms.ModelForm):

    name = forms.CharField(max_length=30, required=True, label=_('CustomTaskCreationFormName'))
    description = forms.CharField(widget=forms.Textarea, max_length=200, required=True, label=_('CustomTaskCreationFormLastName'))

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'performer']
