from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from clients.api.v1.serializer.client_serializer import ClientSerializer
from clients.api.v1.views.client_view import APIListPagination
from clients.models import Balance
from core.filters.product_filters import CategoryFilter


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all().order_by('time_create')
    serializer_class = ClientSerializer
    pagination_class = APIListPagination
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    search_field = ['value']
    ordering_fields = ['client']