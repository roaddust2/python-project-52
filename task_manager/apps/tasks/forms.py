from task_manager.apps.tasks.models import Task
from django import forms
from task_manager.utils.text import FormFields


field = FormFields()


class CustomTaskCreationForm(forms.ModelForm):

    name = forms.CharField(
        max_length=30,
        required=True,
        label=field.task_create_name
    )
    description = forms.CharField(
        widget=forms.Textarea,
        max_length=200,
        required=True,
        label=field.task_create_description
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'performer', 'tags']
