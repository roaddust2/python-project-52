from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=True, label=_('LoginFirstName'))
    last_name = forms.CharField(max_length=30, required=True, label=_('LoginLastName'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
