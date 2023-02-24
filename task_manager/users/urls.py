from django.urls import path
from task_manager.users.views import (
    UsersListView,
    UsersSignUpView,
)


urlpatterns = [
    path('', UsersListView.as_view(), name='users_index'),
    path('create/', UsersSignUpView.as_view(), name='users_signup'),
]
