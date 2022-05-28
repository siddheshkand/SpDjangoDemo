from operator import mod
from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    gst = models.CharField(max_length=15)
    contact = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    buying_price = models.PositiveIntegerField()
    mrp = models.PositiveIntegerField()
    units = models.PositiveIntegerField()
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    unit = models.PositiveIntegerField()    
    def __str__(self):
        return self.customer.name + self.product.name

