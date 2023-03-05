from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.apps.tags.models import Tag


class TagForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, label=_('TagFormName'))

    class Meta:
        model = Tag
        fields = ['name']
