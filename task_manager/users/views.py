from task_manager.users.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
)


# Create your views here.
class UsersListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class UsersSignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = 'login'
