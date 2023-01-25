from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.filters.product_filters import ProductFilter
from product.api.v1.serializer.product_serializer import ProductSerializer
from product.api.v1.views.category_view import APIListPagination
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('time_create')
    serializer_class = ProductSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = ProductFilter
    search_field = ['category', 'name', 'price', 'stock']
    ordering_fields = ['category', 'name', 'price']