from django_filters import rest_framework as filters

from suppliers.models import Supplier


class SupplierFilter(filters.Filter):
    name = filters.CharFilter()
    location = filters.RangeFilter()
    product = filters.CharFilter()
    class Meta:
        model = Supplier
        field = ['name', 'location', 'product']
