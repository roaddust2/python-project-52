from django.urls import path
from task_manager.apps.users.views import (
    UserCreateView,
    UsersListView,
    UserUpdateView,
    UserDeleteView
)


urlpatterns = [
    path('', UsersListView.as_view(), name='users_index'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='users_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='users_delete'),
    path('create/', UserCreateView.as_view(), name='users_create'),
]
