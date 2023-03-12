from django.db import models
from django.contrib.auth.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.labels.models import Label
from task_manager.utils.text import FormFields


field = FormFields()


class Task(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name=field.task_create_name
    )
    description = models.TextField(
        max_length=200,
        verbose_name=field.task_create_description
    )
    author = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='author_of_task'
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='executor_of_task',
        null=True,
        blank=True,
        verbose_name=field.task_create_executor
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT,
        verbose_name=field.task_create_status
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        verbose_name=field.task_create_labels
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
