from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        field = ['first_name', 'second_name', 'age', 'email', 'phone', 'location']