from rest_framework import serializers

from clients.models import Balance


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        field = ['value', 'client']