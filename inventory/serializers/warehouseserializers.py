from rest_framework import serializers
from inventory.models import *
from inventory.serializers.stockserializers import *


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'description', 'address', 'contact']

class WarehouseStockSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True, read_only='True')

    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'description', 'address', 'contact', 'stocks']