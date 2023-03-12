from django.urls import path
from task_manager.apps.tags.views import (
    LabelsListView,
    LabelCreateView,
    LabelUpdateView,
    LabelDeleteView
)


urlpatterns = [
    path('', LabelsListView.as_view(), name='labels_index'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='labels_update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='labels_delete'),
    path('create/', LabelCreateView.as_view(), name='labels_create'),
]
