from django.urls import path
from task_manager.apps.tags.views import (
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)


urlpatterns = [
    path('', TagsListView.as_view(), name='tags_index'),
    path('<int:pk>/update/', TagsUpdateView.as_view(), name='tags_update'),
    path('<int:pk>/delete/', TagsDeleteView.as_view(), name='tags_delete'),
    path('create/', TagsCreateView.as_view(), name='tags_create'),
]
