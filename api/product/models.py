from django.db import models
from django.db.models import CharField, DateTimeField, ForeignKey, BooleanField, ImageField

from api.category.models import Category

class Product(models.Model):
    name = CharField(max_length=50)
    description = CharField(max_length=250)
    category = ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    price = CharField(max_length=50)
    stock = CharField(max_length=50)
    is_active = BooleanField(default=True, blank=True)
    image = ImageField(upload_to='images/', blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name