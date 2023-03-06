from .models import Status
from django import forms
from task_manager.utils.text import FormFields


field = FormFields()


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        required=True,
        label=field.status_create_name
    )

    class Meta:
        model = Status
        fields = ['name']
