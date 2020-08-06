from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

warehouse_list = WarehouseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
warehouse_detail = WarehouseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

stock_list = StockViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
stock_detail = StockViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('warehouses/', warehouse_list, name='warehouse-list'),
    path('warehouses/<int:pk>/', warehouse_detail, name='warehouse-detail'),
    path('stocks/', stock_list, name='stock-list'),
    path('stocks/<int:pk>/', stock_detail, name='stock-detail')
])