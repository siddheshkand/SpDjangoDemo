from django.http import HttpResponse
from django.shortcuts import render
from inventory import models
# Create your views here.
def hello_world(request):
    orders = models.Order.objects.all()
    total_sales = 0
    total_order = 0
    for o in orders:
        total_sales = (o.unit*o.product.mrp) + total_sales
        total_order = (o.unit) + total_order
    return HttpResponse("Total Sales: " + str(total_sales) + " Total order: " + str(total_order)  )