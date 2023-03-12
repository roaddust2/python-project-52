from django.db import models
from task_manager.utils.text import FormFields, Colors


field = FormFields()
color = Colors()


class Label(models.Model):
    RED = 'danger'
    GREEN = 'success'
    BLUE = 'primary'
    GREY = 'secondary'
    COLOR_CHOICES = [
        (GREY, color.gray),
        (GREEN, color.green),
        (BLUE, color.blue),
        (RED, color.red),
    ]
    name = models.CharField(
        max_length=30,
        verbose_name=field.label_create_name,
    )
    color = models.CharField(
        max_length=9,
        choices=COLOR_CHOICES,
        default=GREY,
        verbose_name=field.label_create_color,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
