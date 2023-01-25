from rest_framework import serializers

from product.models import Raiting


class RaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raiting
        field = ['value', 'product']