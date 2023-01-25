from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.filters.suplliers_filters import SupplierFilter
from suppliers.api.v1.serializer.supplier_serializer import SupplierSerializer
from suppliers.models import Supplier


class APIListPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page_side'
    max_page_size = 10


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('time_create')
    serializer_class = SupplierSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    search_field = ['name', 'location', 'product']
    ordering_fields = ['name', 'product']
