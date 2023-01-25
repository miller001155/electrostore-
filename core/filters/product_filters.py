from django_filters import rest_framework as filters

from product.models import Product, Category, Raiting


class ProductFilter(filters.Filter):
    name = filters.CharFilter()
    category = filters.RangeFilter()
    class Meta:
        model = Product
        field = ['first_name', 'second_name', 'price', 'stock']

class CategoryFilter(filters.Filter):
    name = filters.CharFilter()
    class Meta:
        model = Category
        field = ['name']

class RaitingFilter(filters.Filter):
    value = filters.CharFilter()

    class Mete:
        model = Raiting
        field = ['vulue', 'product']