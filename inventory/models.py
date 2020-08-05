from django.db import models


# Create your models here.
class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, blank=True, default='')

class Warehouse(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    contact = models.CharField(max_length=100, blank=True, default='')

class Stock(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    inventoryonhand = models.IntegerField(default=0)
    reorderlevel = models.IntegerField(default=0)
    product = models.ForeignKey(Product, related_name='stocks', on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, related_name='stocks', on_delete=models.CASCADE)

""" ToDo: Functionalities to be included in the next phase

"""