from django.urls import path
from task_manager.apps.tasks.views import (
    TasksListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks_index'),
    path('create/', TaskCreateView.as_view(), name='tasks_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='tasks_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='tasks_delete'),
]