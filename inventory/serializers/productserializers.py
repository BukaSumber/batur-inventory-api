from rest_framework import serializers
from inventory.models import *
from inventory.serializers.stockserializers import *


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']

class ProductStockSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True, read_only='True')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stocks']