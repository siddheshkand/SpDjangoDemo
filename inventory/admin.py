from django.contrib import admin
from inventory import models
# Register your models here.



class MyProductAdmin(admin.ModelAdmin):
    model = models.Product
    list_display = [
        "id",
        "name",
        "description",
        "buying_price",
        "mrp",
        "units",
        "vendor",
    ]
    list_editable=[
        "name",
        "buying_price",
        "mrp",
        "units",
        "vendor",
    ]

class MyVendorAdmin(admin.ModelAdmin):
    model = models.Vendor
    list_display = [
        "name",
        "address",
        "gst",
        "contact",
    ]

class MyCustomerAdmin(admin.ModelAdmin):
    model = models.Customer
    list_display = [
        "name",
        "contact",
    ]


class MyOrderAdmin(admin.ModelAdmin):
    model = models.Order
    list_display = [
        "customer",
        "product",
        "unit",
    ]


admin.site.register(models.Product,MyProductAdmin)
admin.site.register(models.Vendor,MyVendorAdmin)
admin.site.register(models.Customer,MyCustomerAdmin)
admin.site.register(models.Order,MyOrderAdmin)