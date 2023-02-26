from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True, label=_('ustomUserCreationFormFirstName'))
    last_name = forms.CharField(max_length=30, required=True, label=_('ustomUserCreationFormLastName'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
