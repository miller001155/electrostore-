from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.filters.product_filters import RaitingFilter
from product.api.v1.serializer.raiting_serializer import RaitingSerializer
from product.api.v1.views.category_view import APIListPagination
from product.models import Raiting


class RaitingViewSet(viewsets.ModelViewSet):
    queryset = Raiting.objects.all().order_by('time_create')
    serializer_class = RaitingSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = RaitingFilter
    search_field = ['value']
    ordering_fields = ['product', 'value']