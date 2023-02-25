from django.urls import path
from task_manager.users.views import (
    UsersCreateView,
    UsersListView,
    UsersUpdateView,
    UserDeleteView
)


urlpatterns = [
    path('', UsersListView.as_view(), name='users_index'),
    path('<int:pk>/update/', UsersUpdateView.as_view(), name='users_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='users_delete'),
    path('create/', UsersCreateView.as_view(), name='users_signup'),
]
