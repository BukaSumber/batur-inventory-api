from rest_framework import serializers
from inventory.models import *

class StockToProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']

class StockToWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'description']

class StockSerializer(serializers.ModelSerializer):
    product = StockToProductSerializer(many=False, read_only='True')
    warehouse = StockToWarehouseSerializer(many=False, read_only='True')

    class Meta:
        model = Stock
        fields = ['id', 'inventoryonhand', 'reorderlevel', 'product', 'warehouse']