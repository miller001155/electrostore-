from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ['category', 'name', 'description', 'price', 'stock', 'location']