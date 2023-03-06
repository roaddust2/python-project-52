from task_manager.apps.tags.models import Tag
from django import forms
from task_manager.utils.text import FormFields


field = FormFields()


class TagForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        required=True,
        label=field.tag_create_name
    )

    class Meta:
        model = Tag
        fields = ['name']
