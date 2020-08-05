from rest_framework import serializers
from inventory.models import *


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'inventoryonhand', 'reorderlevel']