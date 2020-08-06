from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    fields = ['name', 'description']
admin.site.register(Product, ProductAdmin)

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    fields = ['name', 'description']
admin.site.register(Warehouse, WarehouseAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'inventoryonhand', 'reorderlevel', 'get_productname', 'get_warehousename')
    def get_productname(self, obj):
        return obj.product.name
    get_productname.admin_order_field  = 'product'
    get_productname.short_description = 'Product'

    def get_warehousename(self, obj):
        return obj.warehouse.name
    get_warehousename.admin_order_field  = 'warehouse'
    get_warehousename.short_description = 'Warehouse'

admin.site.register(Stock, StockAdmin)