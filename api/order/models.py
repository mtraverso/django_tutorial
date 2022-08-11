from django.db import models
from django.db.models import ForeignKey, CASCADE, CharField, DateTimeField

from api.user.models import CustomUser
from api.product.models import Product


# Create your models here.
class Order(models.Model):
    user = ForeignKey(CustomUser, CASCADE, null=True, blank=True)
    product_names = CharField(max_length=500)
    total_products = CharField(max_length=500, default=0)
    transaction_id = CharField(max_length=150, default=0)
    total_amount = CharField(max_length=50, default=0)
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)