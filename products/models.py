from django.db import models
from categories.models import Category
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name