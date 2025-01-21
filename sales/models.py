from django.db import models
from products.models import Products
# Create your models here.

class Sales(models.Model):
    product = models.ForeignKey(Products, related_name='sales', on_delete=models.PROTECT)
    quantity = models.IntegerField()
    total = models.FloatField()
    date_of_sale = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name