from django.db import models
from uuid import uuid4


class todos(models.Model):
    title = models.CharField(max_length=40, blank=False)
    todo_content = models.CharField(max_length=400, blank=True)
    date_added = models.DateTimeField(auto_now=True)
    slugg_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)

    def __str__(self):
        return self.title
