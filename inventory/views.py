from inventory.models import *
from inventory.serializers.productserializers import *
from inventory.serializers.warehouseserializers import *
from rest_framework import permissions
from rest_framework import viewsets, renderers
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'warehouses': reverse('warehouse-list', request=request, format=format)
    })

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer