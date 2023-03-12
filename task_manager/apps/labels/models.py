from django.db import models
from task_manager.utils.text import FormFields


field = FormFields()


class Label(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name=field.label_create_name
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
