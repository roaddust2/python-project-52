from django.db import models
from django.contrib.auth.models import User
from task_manager.apps.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_of_task')
    performer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='performer_of_task')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name