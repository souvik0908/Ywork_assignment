from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'title', 'description']
        extra_kwargs = {
            'title': {'required': True, 'allow_blank': False},
            'description': {'required': True, 'allow_blank': False}
        }
        read_only_fields = ['id', 'user']
