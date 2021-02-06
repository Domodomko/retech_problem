from .models import *

# third party
from rest_framework import serializers


class VendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vending
        fields = ('id', 'address', 'max_size', 'count', 'id_key', 'total_sum')


class VendingFillSerializer(serializers.ModelSerializer):
    update = serializers.IntegerField(required=True)

    class Meta:
        model = Vending
        fields = ('update', 'id_key')

    def validate(self, validated_data):
        id_key = validated_data['id_key']
        vend = Vending.objects.get(id_key=id_key)
        update = validated_data['update']

        if ((vend.count+update) > vend.max_size):
            raise serializers.ValidationError(
                {"Count problem"})
        vend.count += update
        return validated_data


class VendingBuySerializer(serializers.ModelSerializer):
    update = serializers.IntegerField(required=True)

    class Meta:
        model = Vending
        fields = ('update', 'id_key')