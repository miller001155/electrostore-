from django_filters import rest_framework as filters

from clients.models import Client, Balance


class ClientsFilter(filters.Filter):
    first_name = filters.CharFilter()

    class Meta:
        model = Client
        field = ['first_name', 'second_name']

class BalanceFilter(filters.Filter):
    value = filters.CharFilter()

    class Meta:
        model = Balance
        field = ['value']