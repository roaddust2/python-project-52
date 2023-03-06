from django.urls import path
from task_manager.apps.tags.views import (
    TagsListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)


urlpatterns = [
    path('', TagsListView.as_view(), name='tags_index'),
    path('<int:pk>/update/', TagUpdateView.as_view(), name='tags_update'),
    path('<int:pk>/delete/', TagDeleteView.as_view(), name='tags_delete'),
    path('create/', TagCreateView.as_view(), name='tags_create'),
]
