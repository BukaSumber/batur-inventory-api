from rest_framework import serializers
from inventory.models import *


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'description', 'address', 'contact']

class WarehouseStockSerializer(serializers.ModelSerializer):
    stocks = serializers.RelatedField(many=True, read_only='True')

    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'description', 'address', 'contact', 'stocks']