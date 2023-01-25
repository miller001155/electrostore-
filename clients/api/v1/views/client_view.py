from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from clients.api.v1.serializer.client_serializer import ClientSerializer
from clients.models import Client
from core.filters.clients_filters import ClientsFilter


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_side'
    max_page_size = 10


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('time_create')
    serializer_class = ClientSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientsFilter
    search_field = ['second_name']
    ordering_fields = ['location']
