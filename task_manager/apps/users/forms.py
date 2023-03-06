from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from task_manager.utils.text import FormFields


field = FormFields()


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=30,
        required=True,
        label=field.user_create_first_name
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label=field.user_create_last_name
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
