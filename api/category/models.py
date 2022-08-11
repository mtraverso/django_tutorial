from django.db import models
from django.db.models import CharField, DateTimeField


class Category(models.Model):
    name= CharField(max_length=50)
    description=CharField(max_length=250)
    created_at=DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name