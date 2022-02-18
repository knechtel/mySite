from rest_framework import serializers

from cadastro.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
