from django.urls import path
from task_manager.apps.statuses.views import (
    StatusesListView,
    StatusCreateView,
    StatusUpdateView,
    StatusDeleteView,
)


urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses_index'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='statuses_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='statuses_delete'),
    path('create/', StatusCreateView.as_view(), name='statuses_create'),
]
