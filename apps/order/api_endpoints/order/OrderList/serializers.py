from rest_framework import serializers

from apps.order.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "cart", "total", "coupon", "full_name", "phone", "region", "district", "note", "payment_type")
