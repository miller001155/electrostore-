from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.filters.product_filters import CategoryFilter
from product.api.v1.serializer.category_serialzer import CategorySerializer
from product.models import Category


class APIListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_side'
    max_page_size = 10
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('time_create')
    serializer_class = CategorySerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    search_field = ['name']
    ordering_fields = ['name']