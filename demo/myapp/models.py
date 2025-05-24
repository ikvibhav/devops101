from django.db import models

# Create your models here.


class TodoItem(models.Model):
    """
    A model representing a to-do item.
    """

    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
